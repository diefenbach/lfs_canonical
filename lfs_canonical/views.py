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
            if url != "":
                Canonical.objects.create(product=product, url=request.POST.get("url"), kind=kind)
        else:
            if url != "":
                canonical.url = url
                canonical.kind = kind
                canonical.save()
            else:
                canonical.delete()

    return render_to_ajax_response(message="Hurz")
