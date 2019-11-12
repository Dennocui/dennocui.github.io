from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from .models import MedicalReport, Injury


class MedicalReportForm(BSModalForm):
    class Meta:
        model = MedicalReport
        fields = '__all__'


class InjuryForm(BSModalForm):
    class Meta:
        model = Injury
        fields = '__all__'
