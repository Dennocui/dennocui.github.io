from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import Events


class EventForm(BSModalForm):
    class Meta:
        model = Events
        fields = '__all__'
