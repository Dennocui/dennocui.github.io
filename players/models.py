import os
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from main.models import Club, Position, HighSchool


# Create your models here.


class Player(models.Model):
    player_name = models.CharField('Player Name', max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField('Email', max_length=254)
    phone_number = models.CharField('Phone Number', max_length=15)
    kin = models.CharField('Next Of Kin', max_length=30)
    kin_contact = models.CharField('Next Of Kin Contact', max_length=15)
    address = models.CharField('Address', max_length=200, null=True)

    birth_cert_no = models.IntegerField('Birth Certificate No', default=0)
    birth_cert_pdf = models.FileField(
        'Birth Certificate PDF', upload_to='files/certs', null=True, blank=True)
    check_cert = models.BooleanField('Verify Cert', default=False)

    passport = models.CharField('Passport No', max_length=150, null=True)
    passport_image = models.FileField(
        'Passport PDF', upload_to='files/passports', null=True, blank=True)
    check_passport = models.BooleanField('Verify Passport', default=False)

    id_number = models.CharField('ID No', max_length=9, null=True)
    id_image = models.FileField(
        'ID PDF', upload_to='files/ids', null=True, blank=True)
    check_id = models.BooleanField('Verify Id', default=False)

    image = models.ImageField(
        'Player Image', upload_to='imgages', null=True, blank=True)

    allergy = models.CharField('Allergies', max_length=200, null=True)
    injury_history = models.CharField(
        'Injury History', max_length=225, null=True)
    skills = models.CharField('Player Skills', max_length=225, null=True)
    about_player = models.CharField('About Player', max_length=225, null=True)

    tertiary_institution = models.CharField(
        'Tertiary Institution', max_length=50, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)
    high_school = models.ForeignKey(
        HighSchool, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(
        'Joined', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.player_name[:25])

    def age(self):
        return timezone.now().year - self.date_of_birth.year

    def verification(self):
        cert = self.check_cert
        passport = self.check_passport
        id = self.check_id

        if cert == True and passport == True and id == True:
            return 1
        elif passport == True and cert == True:
            return 2
        elif id == True and passport == True:
            return 2
        elif id == True and cert == True:
            return 2
        elif id == True:
            return 3
        elif cert == True:
            return 3
        elif passport == True:
            return 3
        return 4

    def cert_name(self):
        return os.path.basename(self.birth_cert_pdf.name)

    def passport_name(self):
        return os.path.basename(self.passport_image.name)

    def id_name(self):
        return os.path.basename(self.id_image.name)

    # def verification(self):
    #     if self.check_cert == True
    #     return
