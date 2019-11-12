from bootstrap_modal_forms.forms import BSModalForm
from .models import Player


class PlayerForm(BSModalForm):
    class Meta:
        model = Player
        fields = '__all__'
