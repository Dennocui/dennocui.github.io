from bootstrap_modal_forms.forms import BSModalForm
from .models import Verify


class VerifyForm(BSModalForm):
    class Meta:
        model = Verify
        fields = '__all__'