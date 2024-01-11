from django.db import models
from django.utils.translation import gettext_lazy as _
from lfs.catalog.models import Product


class Canonical(models.Model):
    """ """

    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
    )
    url = models.CharField(_("URL"), blank=True, max_length=200)
    kind = models.SmallIntegerField(_("Kind"), choices=[[1, _("Canonical")], [2, _("Redirect")]], default=1)
