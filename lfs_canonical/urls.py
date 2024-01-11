from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r"^edit/(?P<product_id>[-\w]+)$", views.edit_canonical, name="lfs_canonical_edit"),
]
