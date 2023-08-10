import markdown
from django import template
from django.utils.safestring import mark_safe
# 템플릿 필터 함수 만들기
register = template.Library()

@register.filter
def sub(value , arg):
    return value - arg

# 마크다운 사용하기 
@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))