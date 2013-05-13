from django.template import Template, RequestContext, Library
from django.template.defaultfilters import stringfilter

import markdown as md

register = Library()

@register.filter(name="markdown", is_safe=True)
@stringfilter
def markdown(value):
  rendered_value = Template(value).render(RequestContext({}))
  return md.markdown(rendered_value, extensions=["tables"])
