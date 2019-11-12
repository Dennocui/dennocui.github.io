import os
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# from players.models import Player


class Club(models.Model):
    name = models.CharField('Club Name', max_length=20)
    coach_name = models.CharField('Coach Name', blank=True, max_length=30)
    coach_contact = models.CharField(
        'Coach Contact', blank=True, max_length=15)
    team_manager = models.CharField('Team Manager', blank=True, max_length=30)
    team_manager_contact = models.CharField(
        'Team Manager Contact', blank=True, max_length=15)
    main_grounds = models.CharField(
        'Main Grounds', blank=True, null=True, max_length=30)
    alt_grounds = models.CharField(
        'Alt Grounds', blank=True, null=True, max_length=30)
    region = models.CharField(
        'Club Region', blank=True, null=True, max_length=30)
    logo = models.ImageField(
        'Club Logo', upload_to='club logos', null=True, blank=True)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class ClubAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user


class HighSchool(models.Model):
    name = models.CharField('High School Name', max_length=225)
    location = models.CharField('School Location', max_length=100)
    patron = models.CharField('School Patron', max_length=100)
    patron_contact = models.CharField('Patron Contact', max_length=15)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField('Field Position', max_length=20)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
