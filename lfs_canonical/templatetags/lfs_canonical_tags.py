from django import template
from django.utils.safestring import mark_safe
from django.template import Library
from django.template import RequestContext
from django.template.loader import render_to_string

from ..models import Canonical
from ..forms import CanonicalForm

register = Library()


@register.simple_tag(takes_context=True)
def canonical_management(context, product):
    request = context.get("request")
    try:
        canonical = Canonical.objects.get(product=product)
    except Canonical.DoesNotExist:
        canonical = None

    result = render_to_string(
        "lfs_canonical/lfs_canonical.html",
        RequestContext(
            request, {"product": product, "canonical": canonical, "form": CanonicalForm(instance=canonical)}
        ),
    )

    return mark_safe(result)


class CanonicalNode(template.Node):
    def render(self, context):
        context["canonical"] = None

        try:
            product = context["product"]
        except KeyError:
            return ""

        try:
            canonical = Canonical.objects.get(product=product)
        except Canonical.DoesNotExist:
            pass
        else:
            if canonical.url and (canonical.kind == 1):
                context["canonical"] = canonical
        return ""


@register.tag
def canonical(parser, token):
    return CanonicalNode()
