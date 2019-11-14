import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from main.models import Club, Position, HighSchool
from datetime import datetime, date


# Create your models here.


class Player(models.Model):
    player_name = models.CharField('Player Name', max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField('Email', max_length=254)
    phone_number = models.CharField('Phone Number', max_length=15)
    kin = models.CharField('Next Of Kin', max_length=30)
    kin_contact = models.CharField('Next Of Kin Contact', max_length=15)
    address = models.CharField('Address', max_length=200, null=True)

    image = models.ImageField('Player Image', upload_to='imgages', null=True, blank=True)

    allergy = models.CharField('Allergies', max_length=200, null=True)
    about_player = models.CharField('About Player', max_length=225, null=True)
    tertiary_institution = models.CharField('Tertiary Institution', max_length=50, null=True)
    injury_history = models.CharField('Injury History', max_length=225, null=True)

    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    high_school = models.ForeignKey(HighSchool, on_delete=models.CASCADE, null=True)

    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    created_at = models.DateTimeField('Joined', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.player_name[:25])

    def age(self):
        today = date.today()
        birthday = self.date_of_birth

        return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        


        
