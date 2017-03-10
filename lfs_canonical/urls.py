from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^edit/(?P<product_id>[-\w]+)$', views.edit_canonical, name='lfs_canonical_edit'),
]
