from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views import generic
from datetime import datetime, date, timedelta
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from bootstrap_modal_forms.generic import BSModalCreateView
import json
from django.db.models import Count, Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import ClubForm, SignUpForm, ClubAdminForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from . models import Club, ClubAdmin, HighSchool, Position
from medical.models import MedicalReport
from players.models import Player

from django.utils.safestring import mark_safe
# import calendar
# from .filters import PlayerFilter


@login_required
def dashboard(request):

    total_players = Player.objects.count()
    injuries = MedicalReport.objects.count()
    club_count = Club.objects.count()
    schools = HighSchool.objects.count()

    dataset = Position.objects.values('name').annotate(
        player_count=Count('player')).order_by('id')
    # .order_by('position')

    positions = list()
    player_series_data = list()

    for entry in dataset:
        positions.append(entry['name'])
        player_series_data.append(entry['player_count'])

    club_dataset = Club.objects.values('name').annotate(
        player_count=Count('player')).order_by('id')
    # .order_by('position')

    clubs = list()
    player_data = list()

    for entry in club_dataset:
        clubs.append(entry['name'])
        player_data.append(entry['player_count'])

    return render(request, 'main/index.html', {
        'positions': json.dumps(positions),
        'player_series_data': json.dumps(player_series_data),
        'clubs': json.dumps(clubs),
        'player_data': json.dumps(player_data),
        'total_players': total_players,
        'injuries': injuries,
        'club_count': club_count,
        'schools': schools,

    })


# def calender(request):
#     return render(request, 'main/calender.html')


# Create
class ClubAdminCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'main/create.html'
    form_class = ClubAdminForm
    success_message = 'Success: Club Admin was created.'
    success_url = reverse_lazy('accounts:users_list')


'''Club Views '''


class ClubListView(LoginRequiredMixin, generic.ListView):
    model = Club
    context_object_name = 'clubs'
    template_name = 'main/list.html'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(ClubListView, self).get_context_data(**kwargs)
        clubs = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(clubs, self.paginate_by)
        try:
            clubs = paginator.page(page)
        except PageNotAnInteger:
            clubs = paginator.page(1)
        except EmptyPage:
            clubs = paginator.page(paginator.num_pages)
        context['clubs'] = clubs
        return context


# Create
class ClubCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'main/create.html'
    form_class = ClubForm
    success_message = 'Success: Club was created.'
    success_url = reverse_lazy('main:club_list')

# Update


class ClubUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Club
    template_name = 'main/update.html'
    context_object_name = 'club'
    form_class = ClubForm
    success_message = 'Success: Club was updated.'
    success_url = reverse_lazy('main:club_list')


# Read


class ClubDetailView(LoginRequiredMixin, BSModalReadView):
    model = Club
    template_name = 'main/club_details.html'

# Delete


class ClubDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Club
    template_name = 'main/delete.html'
    success_message = 'Success: Club was deleted.'
    success_url = reverse_lazy('main:club_list')
