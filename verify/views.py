from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
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
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import VerifyForm
from . models import Verify

@login_required
def dashboard(request):

    # total_players = Player.objects.count()
    verify = Verify.objects.count()
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


    return render(request, 'verify/index.html'
    , {
    #     'positions': json.dumps(positions),
    #     'player_series_data': json.dumps(player_series_data),
    #     'clubs': json.dumps(clubs),
    #     'player_data': json.dumps(player_data),
    #     'total_players': total_players,
        'verify': verify,
    #     'club_count': club_count,
    #     'schools': schools ,

    }
    )


class VerifyListView(LoginRequiredMixin, generic.ListView):
    model = Verify
    context_object_name = 'verify'
    template_name = 'verify/verify.html'
    paginate_by = 10
    ordering = ['-player']

    def get_context_data(self, **kwargs):
        context = super(VerifyListView, self).get_context_data(**kwargs)
        verify = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(verify, self.paginate_by)
        try:
            verify = paginator.page(page)
        except PageNotAnInteger:
            verify = paginator.page(1)
        except EmptyPage:
            verify = paginator.page(paginator.num_pages)
        context['verify'] = verify
        return context

# Create
class VerifyCreateView(BSModalCreateView):
    template_name = 'verify/create.html'
    form_class = VerifyForm
    success_message = 'Success: Verification  was created.'
    success_url = reverse_lazy('verify:verify')

#Update
class VerifyUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Verify
    template_name = 'verify/verify_update.html'
    context_object_name = 'verify'
    form_class = VerifyForm
    success_message = 'Success: Player was Verified Successfuly.'
    success_url = reverse_lazy('verify:verify')


#Update
class UpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Verify
    template_name = 'verify/update.html'
    context_object_name = 'verify'
    form_class = VerifyForm
    success_message = 'Success: Player was Verified Successfuly.'
    success_url = reverse_lazy('verify:verify')



# Read
class VerifyDetailView(BSModalReadView):
    model = Verify
    template_name = 'verify/detail.html'

# Delete
class VerifyDeleteView(BSModalDeleteView):
    model = Verify
    template_name = 'verify/delete.html'
    success_message = 'Success: Injury  was deleted.'
    success_url = reverse_lazy('verify:verify')