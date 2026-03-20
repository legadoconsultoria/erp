from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Adiciona classe(s) CSS a um campo de formulário.

    Uso no template:
        {{ form.field|add_class:"form-control" }}
    """
    try:
        existing = field.field.widget.attrs.get('class', '')
        classes = (existing + ' ' + css_class).strip()
        return field.as_widget(attrs={**field.field.widget.attrs, 'class': classes})
    except Exception:
        return field
