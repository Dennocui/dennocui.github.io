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


from .forms import ConditioningForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from . models import Conditioning

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
class ConditioninglCreateView(BSModalCreateView):
    template_name = 'snc/create.html'
    form_class = ConditioningForm
    success_message = 'Success: Conditioning Report was created.'
    success_url = reverse_lazy('snc:list')

# Update


class ConditioningUpdateView(BSModalUpdateView):
    model = Conditioning
    template_name = 'snc/update.html'
    context_object_name = ''
    form_class = ConditioningForm
    success_message = 'Success: Conditioning Report was updated.'
    success_url = reverse_lazy('snc:list')


# Read


class ConditioningDetailView(BSModalReadView):
    model = Conditioning
    context_object_name = 'conditionings'
    # queryset = Conditioning.objects.select_related()
    template_name = 'snc/detail.html'


# Delete


class ConditioningDeleteView(BSModalDeleteView):
    model = Conditioning
    template_name = 'snc/delete.html'
    success_message = 'Success: Conditioning Report was deleted.'
    success_url = reverse_lazy('snc:list')
