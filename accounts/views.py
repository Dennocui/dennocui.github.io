from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from main.models import ClubAdmin

from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import CustomUserCreationForm


class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('accounts:index')


class UserListView(generic.ListView):
    model = ClubAdmin
    context_object_name = 'users'
    template_name = 'accounts/user_list.html'
    paginate_by = 10
    ordering = ['user']

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        users = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(users, self.paginate_by)
        try:
            users = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        context['users'] = users
        return context


# Update


class UserUpdateView(BSModalUpdateView):
    model = User
    template_name = 'accounts/update.html'
    context_object_name = 'user'
    form_class = CustomUserCreationForm
    success_message = 'Success: User was updated.'
    success_url = reverse_lazy('accounts:users_list')


# Read


class UserDetailView(BSModalReadView):
    model = User
    template_name = 'accounts/user_detail.html'

# Delete


class UserDeleteView(BSModalDeleteView):
    model = User
    template_name = 'accounts/delete.html'
    success_message = 'Success: User was deleted.'
    success_url = reverse_lazy('accounts:users_list')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect to Home
            return HttpResponseRedirect(reverse('main:dashboard'))
        else:
            messages.error(request, 'Bad Username or Password')

    return render(request, 'accounts/signin.html', {})


def logout_user(request):
    # return render(request, 'accounts/logout.html', {})
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
