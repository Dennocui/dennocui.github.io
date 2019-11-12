from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def signin(request):

    context = {}
    # return render(request,'accounts/login.html', context)
    return HttpResponseRedirect(reverse('accounts:login'))
