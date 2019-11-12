from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import Conditioning


class ConditioningForm(BSModalForm):
    class Meta:
        model = Conditioning
        fields = '__all__'
