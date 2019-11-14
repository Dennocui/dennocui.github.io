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

from .forms import PlayerForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from . models import Player
from medical.models import MedicalReport


from django.utils.safestring import mark_safe
# import calendar
from .filters import PlayerFilter
from . models import Player


'''
Views for Player Model
'''


class PlayerListView(LoginRequiredMixin, generic.ListView):
    model = Player
    context_object_name = 'players'
    template_name = 'players/list.html'
    paginate_by = 10
    ordering = ['player_name']

    def get_context_data(self, **kwargs):
        context = super(PlayerListView, self).get_context_data(**kwargs)
        players = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(players, self.paginate_by)
        try:
            players = paginator.page(page)
        except PageNotAnInteger:
            players = paginator.page(1)
        except EmptyPage:
            players = paginator.page(paginator.num_pages)
        context['players'] = players
        return context


# Create
class PlayerCreateView(LoginRequiredMixin, BSModalCreateView):
    template_name = 'players/create.html'
    form_class = PlayerForm
    success_message = 'Success: Player was created.'
    success_url = reverse_lazy('players:player_list')

# Update


class PlayerUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Player
    template_name = 'players/update.html'
    context_object_name = 'player'
    form_class = PlayerForm
    success_message = 'Success: Player was updated.'
    success_url = reverse_lazy('players:player_list')


# Read


class PlayerDetailView(LoginRequiredMixin, BSModalReadView):
    model = Player
    # context_object_name = 'players'
    template_name = 'players/detail.html'

# Delete


class PlayerDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Player
    template_name = 'players/delete.html'
    success_message = 'Success: Player was deleted.'
    success_url = reverse_lazy('players:player_list')
