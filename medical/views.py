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
from bootstrap_modal_forms.generic import BSModalCreateView


from .forms import MedicalReportForm, InjuryForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from . models import MedicalReport, Injury


@login_required
def dashboard(request):

    # total_players = Player.objects.count()
    injuries = MedicalReport.objects.count()
    # club_count = Club.objects.count()
    # schools = HighSchool.objects.count()


    # dataset = Position.objects.values('name').annotate(player_count=Count('player')).order_by('id')
    # # .order_by('position')


    # positions = list()
    # player_series_data = list()


    # for entry in dataset:
    #     positions.append(entry['name'])
    #     player_series_data.append(entry['player_count'])


    # club_dataset = Club.objects.values('name').annotate(player_count=Count('player')).order_by('id')
    # # .order_by('position')


    # clubs = list()
    # player_data = list()


    # for entry in club_dataset:
    #     clubs.append(entry['name'])
    #     player_data.append(entry['player_count'])


    return render(request, 'medical/index.html'
    , {
    #     'positions': json.dumps(positions),
    #     'player_series_data': json.dumps(player_series_data),
    #     'clubs': json.dumps(clubs),
    #     'player_data': json.dumps(player_data),
    #     'total_players': total_players,
        'injuries': injuries,
    #     'club_count': club_count,
    #     'schools': schools ,

    }
    )

''' 
Views for MedicalReport Model
'''


class MedicalListView(generic.ListView):
    model = MedicalReport
    context_object_name = 'medicals'
    template_name = 'medical/list.html'
    paginate_by = 15
    ordering = ['-recovery_date']

    def get_context_data(self, **kwargs):
        context = super(MedicalListView, self).get_context_data(**kwargs)
        medicals = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(medicals, self.paginate_by)
        try:
            medicals = paginator.page(page)
        except PageNotAnInteger:
            medicals = paginator.page(1)
        except EmptyPage:
            medicals = paginator.page(paginator.num_pages)
        context['medicals'] = medicals
        return context


# Create
class MedicalCreateView(BSModalCreateView):
    template_name = 'medical/create.html'
    form_class = MedicalReportForm
    success_message = 'Success: MedicalReport was created.'
    success_url = reverse_lazy('medical:list')

# Update


class MedicalUpdateView(BSModalUpdateView):
    model = MedicalReport
    template_name = 'medical/update.html'
    context_object_name = 'medical'
    form_class = MedicalReportForm
    success_message = 'Success: MedicalReport was updated.'
    success_url = reverse_lazy('medical:list')


# Read


class MedicalDetailView(BSModalReadView):
    model = MedicalReport
    template_name = 'medical/detail.html'

# Delete


class MedicalDeleteView(BSModalDeleteView):
    model = MedicalReport
    template_name = 'main/delete.html'
    success_message = 'Success: Medical Report was deleted.'
    success_url = reverse_lazy('medical:list')





''' 
Views for Injury Model
'''


class InjuryListView(generic.ListView):
    model = Injury
    context_object_name = 'injuries'
    template_name = 'medical/injury_list.html'
    paginate_by = 15
    ordering = ['-injury_type']

    def get_context_data(self, **kwargs):
        context = super(InjuryListView, self).get_context_data(**kwargs)
        injuries = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(injuries, self.paginate_by)
        try:
            injuries = paginator.page(page)
        except PageNotAnInteger:
            injuries = paginator.page(1)
        except EmptyPage:
            injuries = paginator.page(paginator.num_pages)
        context['injuries'] = injuries
        return context


# Create
class InjuryCreateView(BSModalCreateView):
    template_name = 'medical/create_injury.html'
    form_class = InjuryForm
    success_message = 'Success: Injury was created.'
    success_url = reverse_lazy('medical:injuries')

# Update


class InjuryUpdateView(BSModalUpdateView):
    model = Injury
    template_name = 'medical/update_injury.html'
    context_object_name = 'injury'
    form_class = InjuryForm
    success_message = 'Success: Injury was updated.'
    success_url = reverse_lazy('medical:injuries')


# Read


class InjuryDetailView(BSModalReadView):
    model = Injury
    template_name = 'medical/injury_detail.html'

# Delete


class InjuryDeleteView(BSModalDeleteView):
    model = Injury
    template_name = 'medical/delete.html'
    success_message = 'Success: Injury  was deleted.'
    success_url = reverse_lazy('medical:injuries')

    