from django import forms
from bootstrap_modal_forms.forms import BSModalForm


from .models import Conditioning, TechnicalSkill, TacticleSkill, MentalSkill, PhysicalSkill, LeadershipSkill

class ConditioningForm(BSModalForm):
    class Meta:
        model = Conditioning
        fields = '__all__'


class LeadershipSkillForm(BSModalForm):
    class Meta:
        model = LeadershipSkill
        fields = '__all__'


class TechnicalSkillForm(BSModalForm):
    class Meta:
        model = TechnicalSkill
        fields = '__all__'



class TacticleSkillForm(BSModalForm):
    class Meta:
        model = TacticleSkill
        fields = '__all__'



class MentalSkillForm(BSModalForm):
    class Meta:
        model = MentalSkill
        fields = '__all__'


class PhysicalSkillForm(BSModalForm):
    class Meta:
        model = PhysicalSkill
        fields = '__all__'

