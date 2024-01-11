from django import forms
from .models import Canonical


class CanonicalForm(forms.ModelForm):
    """
    Form to edit bank account.
    """

    class Meta:
        model = Canonical
        exclude = ("product",)
