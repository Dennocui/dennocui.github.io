from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from .forms import ConditioningForm , TechnicalSkillForm, TacticleSkillForm, MentalSkillForm, PhysicalSkillForm, LeadershipSkillForm
from . models import Conditioning, TechnicalSkill, TacticleSkill, MentalSkill, PhysicalSkill, LeadershipSkill

# Create your views here.


class ConditioningListView(generic.ListView):
    model = Conditioning
    context_object_name = 'conditionings'
    template_name = 'snc/list.html'
    paginate_by = 15
    ordering = ['created_at']

    def get_context_data(self, **kwargs):
        context = super(ConditioningListView, self).get_context_data(**kwargs)
        conditionings = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(conditionings, self.paginate_by)
        try:
            conditionings = paginator.page(page)
        except PageNotAnInteger:
            conditionings = paginator.page(1)
        except EmptyPage:
            conditionings = paginator.page(paginator.num_pages)
        context['conditionings'] = conditionings
        return context


# Create
class ConditioningCreateView(BSModalCreateView):
    template_name = 'snc/create.html'
    form_class = ConditioningForm
    success_message = 'Success: Conditioning Report was created.'
    success_url = reverse_lazy('snc:list')

# Update
class ConditioningUpdateView(BSModalUpdateView):
    model = Conditioning
    template_name = 'snc/update.html'
    context_object_name = 'conditioning'
    form_class = ConditioningForm
    success_message = 'Success: Conditioning Report was updated.'
    success_url = reverse_lazy('snc:list')

# Read
class ConditioningDetailView(BSModalReadView):
    model = Conditioning
    template_name = 'snc/detail.html'

# Delete
class ConditioningDeleteView(BSModalDeleteView):
    model = Conditioning
    template_name = 'snc/delete.html'
    success_message = 'Success: Conditioning Report was deleted.'
    success_url = reverse_lazy('snc:list')



'''Technical technical'''

class TechnicalListView(generic.ListView):
    model = TechnicalSkill
    context_object_name = 'technicals'
    template_name = 'snc/technical_list.html'
    paginate_by = 15
    ordering = ['created_at']

    def get_context_data(self, **kwargs):
        context = super(TechnicalListView, self).get_context_data(**kwargs)
        technicals = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(technicals, self.paginate_by)
        try:
            technicals = paginator.page(page)
        except PageNotAnInteger:
            technicals = paginator.page(1)
        except EmptyPage:
            technicals = paginator.page(paginator.num_pages)
        context['technicals'] = technicals
        return context

# Create
class TechnicalCreateView(BSModalCreateView):
    template_name = 'snc/create.html'
    form_class = TechnicalSkillForm
    success_message = 'Success: technicals Report was created.'
    success_url = reverse_lazy('snc:technical_list')

# Update
class TechnicalUpdateView(BSModalUpdateView):
    model = TechnicalSkill
    template_name = 'snc/update.html'
    context_object_name = 'technicalskill'
    form_class = TechnicalSkillForm
    success_message = 'Success: Technical Report was updated.'
    success_url = reverse_lazy('snc:technical_list')

# Read
class TechnicalDetailView(BSModalReadView):
    model = TechnicalSkill
    template_name = 'snc/detail.html'


'''Tacticle'''

class TacticleListView(generic.ListView):
    model = TacticleSkill
    context_object_name = 'tacticles'
    template_name = 'snc/tacticle_list.html'
    paginate_by = 15
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super(TacticleListView, self).get_context_data(**kwargs)
        tacticles = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(tacticles, self.paginate_by)
        try:
            tacticles = paginator.page(page)
        except PageNotAnInteger:
            tacticles = paginator.page(1)
        except EmptyPage:
            tacticles = paginator.page(paginator.num_pages)
        context['tacticles'] = tacticles
        return context


# Create
class TacticleCreateView(BSModalCreateView):
    template_name = 'snc/create.html'
    form_class = TacticleSkillForm
    success_message = 'Success: Tacticles Report was created.'
    success_url = reverse_lazy('snc:tacticle_list')

# Update
class TacticleUpdateView(BSModalUpdateView):
    model = TacticleSkill
    template_name = 'snc/update.html'
    context_object_name = 'tacticleskill'
    form_class = TacticleSkillForm
    success_message = 'Success: Tacticle Report was updated.'
    success_url = reverse_lazy('snc:tacticle_list')

# Read
class TacticleDetailView(BSModalReadView):
    model = TacticleSkill
    template_name = 'snc/detail.html'


'''Mental'''

class MentalListView(generic.ListView):
    model = MentalSkill
    context_object_name = 'mentals'
    template_name = 'snc/mental_list.html'
    paginate_by = 15
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super(MentalListView, self).get_context_data(**kwargs)
        mentals = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(mentals, self.paginate_by)
        try:
            mentals = paginator.page(page)
        except PageNotAnInteger:
            mentals = paginator.page(1)
        except EmptyPage:
            mentals = paginator.page(paginator.num_pages)
        context['mentals'] = mentals
        return context


# Create
class MentalCreateView(BSModalCreateView):
    template_name = 'snc/create.html'
    form_class = MentalSkillForm
    success_message = 'Success: Mental Report was created.'
    success_url = reverse_lazy('snc:mental_list')

# Update
class MentalUpdateView(BSModalUpdateView):
    model = MentalSkill
    template_name = 'snc/update.html'
    context_object_name = 'mentalskill'
    form_class = MentalSkillForm
    success_message = 'Success: Mental Report was updated.'
    success_url = reverse_lazy('snc:mental_list')

# Read
class MentalDetailView(BSModalReadView):
    model = MentalSkill
    template_name = 'snc/detail.html'


'''PhysicalSkill'''

class PhysicalListView(generic.ListView):
    model = PhysicalSkill
    context_object_name = 'physicals'
    template_name = 'snc/physical_list.html'
    paginate_by = 15
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super(PhysicalListView, self).get_context_data(**kwargs)
        physicals = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(physicals, self.paginate_by)
        try:
            physicals = paginator.page(page)
        except PageNotAnInteger:
            physicals = paginator.page(1)
        except EmptyPage:
            physicals = paginator.page(paginator.num_pages)
        context['physicals'] = physicals
        return context


# Create
class PhysicalCreateView(BSModalCreateView):
    template_name = 'snc/create.html'
    form_class = PhysicalSkillForm
    success_message = 'Success: physical Report was created.'
    success_url = reverse_lazy('snc:physical_list')

# Update
class PhysicalUpdateView(BSModalUpdateView):
    model = PhysicalSkill
    template_name = 'snc/update.html'
    context_object_name = 'physicalskill'
    form_class = PhysicalSkillForm
    success_message = 'Success: Physical Report was updated.'
    success_url = reverse_lazy('snc:physical_list')

# Read
class PhysicalDetailView(BSModalReadView):
    model = PhysicalSkill
    template_name = 'snc/detail.html'
    

'''LeadershipSkill'''

class LeadershipListView(generic.ListView):
    model = LeadershipSkill
    context_object_name = 'leaderships'
    template_name = 'snc/leadership_list.html'
    paginate_by = 15
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super(LeadershipListView, self).get_context_data(**kwargs)
        leadership = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(leadership, self.paginate_by)
        try:
            leadership = paginator.page(page)
        except PageNotAnInteger:
            leadership = paginator.page(1)
        except EmptyPage:
            leadership = paginator.page(paginator.num_pages)
        context['leadership'] = leadership
        return context


# Create
class LeadershipCreateView(BSModalCreateView):
    template_name = 'snc/create.html'
    form_class = LeadershipSkillForm
    success_message = 'Success: Leadership Report was created.'
    success_url = reverse_lazy('snc:leadership_list')

# Update
class LeadershipUpdateView(BSModalUpdateView):
    model = LeadershipSkill
    template_name = 'snc/update.html'
    context_object_name = 'leadershipskill'
    form_class = LeadershipSkillForm
    success_message = 'Success: Leadership Report was updated.'
    success_url = reverse_lazy('snc:leadership_list')

# Read
class LeadershipDetailView(BSModalReadView):
    model = LeadershipSkill
    template_name = 'snc/detail.html'
    