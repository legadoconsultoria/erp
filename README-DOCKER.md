# 🐳 ERP System - Docker Setup & Deployment

Guia completo para executar o ERP System em Docker.

## 📋 Pré-requisitos

- Docker >= 20.10
- Docker Compose >= 1.29
- Git (opcional)

## 🚀 Início Rápido

### 1. Clone/Navegue até o projeto
```bash
cd z:\ERP\ERP\ Codigo\erp
```

### 2. Criar arquivo `.env` a partir do example
```bash
# Windows (PowerShell)
Copy-Item .env.example .env

# Linux/Mac
cp .env.example .env
```

### 3. Editar `.env` conforme necessário (opcional para desenvolvimento)
```env
DEBUG=True  # False em produção
SECRET_KEY=sua-chave-secreta-aqui
DB_PASSWORD=sua-senha-postgres
```

### 4. Iniciar os containers
```bash
# Com SQLite (mais simples)
docker-compose up -d

# Ou com PostgreSQL
docker-compose -f docker-compose.yml up -d
```

### 5. Executar migrations
```bash
docker-compose exec web python manage.py migrate
```

### 6. Criar superusuário (admin)
```bash
docker-compose exec web python manage.py createsuperuser
```

### 7. Coletar arquivos estáticos (se usar Nginx)
```bash
docker-compose exec web python manage.py collectstatic --noinput
```

## ✅ Verificar se está funcionando

- **Aplicação**: http://localhost:8000
- **Admin**: http://localhost:8000/admin
- **Nginx**: http://localhost (se ativado)

## 📁 Estrutura de Containers

```
erp_network
├── erp_web (Django + Gunicorn)
│   ├── Port: 8000
│   └── Volumes: ./:/app
├── erp_db (PostgreSQL)
│   ├── Port: 5432
│   └── Volume: postgres_data
└── erp_nginx (Nginx - opcional)
    ├── Port: 80/443
    └── Volumes: static, media
```

## 🔧 Comandos Úteis

### Logs
```bash
# Ver logs de um serviço
docker-compose logs -f web       # Django logs
docker-compose logs -f db        # Database logs

# Ver últimas 50 linhas
docker-compose logs --tail=50 web
```

### SSH/Bash no Container
```bash
docker-compose exec web bash
```

### Executar Comandos Django
```bash
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py shell
docker-compose exec web python manage.py dumpdata > backup.json
```

### Backup do Banco de Dados
```bash
# PostgreSQL
docker-compose exec db pg_dump -U postgres erp_db > backup.sql

# Restaurar backup
docker-compose exec -T db psql -U postgres erp_db < backup.sql
```

### Parar os Containers
```bash
docker-compose down
```

### Remover Volumes (CUIDADO - deleta dados)
```bash
docker-compose down -v
```

### Rebuild da Imagem (se alterou Dockerfile)
```bash
docker-compose build --no-cache
docker-compose up -d
```

## 🔐 Configuração Para Produção

### 1. Atualizar `.env`
```env
DEBUG=False
SECRET_KEY=gerar-chave-segura-aqui
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
DB_PASSWORD=senha-muito-segura

# SSL/TLS (se tiver certificados)
SECURE_SSL_REDIRECT=True
```

### 2. Gerar SECRET_KEY Segura
```bash
docker-compose exec web python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 3. Ativar Nginx (descomente no docker-compose.yml)
```yaml
  nginx:
    # ... remova os comentários
```

### 4. Configurar SSL/TLS
Coloque certificados em `./certs/cert.pem` e `./certs/key.pem`, depois descomente a seção SSL no `nginx.conf`.

### 5. Usar PostgreSQL em Produção
Já está configurado no `docker-compose.yml`. Basta:
```bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=erp_db
DB_USER=postgres
DB_PASSWORD=sua-senha-segura
DB_HOST=db
```

### 6. Deploy em Servidor
```bash
# SSH no servidor
ssh user@seu-servidor.com

# Clone o repositório
git clone seu-repo-url
cd seu-repo

# Copie e configure o .env
cp .env.example .env
# Edite conforme necessário

# Inicie os containers
docker-compose -f docker-compose.prod.yml up -d
```

## 📊 Performance & Escalabilidade

### Aumentar Workers (Gunicorn)
No `Dockerfile`, altere:
```dockerfile
gunicorn core_erp.wsgi:application --bind 0.0.0.0:8000 --workers 8
```

### Redis Cache (opcional)
Adicione ao `docker-compose.yml`:
```yaml
redis:
  image: redis:7-alpine
  ports:
    - "6379:6379"
```

E configure em `settings.py`:
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
    }
}
```

## 🐛 Troubleshooting

### Erro: "Cannot connect to Docker daemon"
```bash
# Reinicie o Docker Desktop ou o daemon
sudo systemctl restart docker  # Linux
```

### Erro: "Port 8000 already in use"
```bash
# Use uma porta diferente
docker-compose -p erp_prod up -d
# Ou altere no docker-compose.yml
```

### Erro: "Permission denied" no volume
```bash
# Ajuste permissões
chmod -R 755 .
```

### Banco de dados vazio
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py loaddata seu-fixture.json  # Se houver
```

## 📚 Recursos Adicionais

- [Docker Docs](https://docs.docker.com/)
- [Docker Compose Docs](https://docs.docker.com/compose/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/)
- [Gunicorn Docs](https://gunicorn.org/)

## 📝 Notas

- Arquivos estáticos e de mídia são persistidos em volumes Docker
- Logs ficam em `./logs/` shared com o container
- Backup automático recomendado para produção
- Use `docker-compose.prod.yml` (se criar) para produção com diferentes configurações

---

**Precisa de ajuda?** Verifique os logs:
```bash
docker-compose logs -f web
```
