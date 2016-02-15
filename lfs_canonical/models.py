from django.db import models
from django.utils.translation import ugettext_lazy as _
from lfs.catalog.models import Product


class Canonical(models.Model):
    """
    """
    product = models.ForeignKey(Product, verbose_name=_(u"Product"))
    url = models.CharField(_(u"URL"), blank=True, max_length=200)
    kind = models.SmallIntegerField(_(u"Kind"), choices=[[1, _(u"Canonical")], [2, _(u"Redirect")]], default=1)
