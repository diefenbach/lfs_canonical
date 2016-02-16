# coding=utf-8
from lfs.catalog.models import Product
from lfs.core.utils import render_to_ajax_response
from . models import Canonical


def edit_canonical(request, product_id):
    """
    """
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        pass
    else:
        url = request.POST.get("url", "")
        kind = request.POST.get("kind")
        try:
            canonical = Canonical.objects.get(product=product)
        except Canonical.DoesNotExist:
            message = u"Canonical wurde angelegt"
            if url != "":
                Canonical.objects.create(product=product, url=request.POST.get("url"), kind=kind)
        else:
            if url != "":
                message = u"Canonical wurde aktualisiert"
                canonical.url = url
                canonical.kind = kind
                canonical.save()
            else:
                message = u"Canonical wurde gelöscht"
                canonical.delete()

    return render_to_ajax_response(message=message)
