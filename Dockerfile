FROM python:3.13-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Instalar dependências do sistema operacional
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho do container
WORKDIR /app

# Copiar arquivo requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar projeto para dentro do container
COPY . .

# Criar diretórios para mídia, arquivos estáticos e logs
RUN mkdir -p /app/staticfiles /app/media /app/logs

# Coletar arquivos estáticos (se houver)
RUN python manage.py collectstatic --noinput --clear 2>/dev/null || true

# Expor porta 8000
EXPOSE 8000

# Copiar script de entrada do container
COPY docker-entrypoint.sh /app/
RUN chmod +x /app/docker-entrypoint.sh

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["gunicorn", "core_erp.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
