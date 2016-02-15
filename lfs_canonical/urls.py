# django imports
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('lfs_canonical.views',
    url(r'^edit/(?P<product_id>[-\w]+)$', "edit_canonical", name='lfs_canonical_edit'),
)
