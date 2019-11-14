import os
from django.db import models
from players.models import Player

# Create your models here.

class Verify(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True,)
            
    birth_cert_no = models.IntegerField('Birth Certificate No', default=0)
    birth_cert_pdf = models.FileField('Birth Certificate PDF', upload_to='files/certs', null=True, blank=True)
    check_cert = models.BooleanField('Verify Cert', default=False)

    passport = models.CharField('Passport No', max_length=150, null=True)
    passport_image = models.FileField('Passport PDF', upload_to='files/passports', null=True, blank=True)
    check_passport = models.BooleanField('Verify Passport', default=False)

    id_number = models.CharField('ID No', max_length=9, null=True)
    id_image = models.FileField('ID PDF', upload_to='files/ids', null=True, blank=True)
    check_id = models.BooleanField('Verify Id', default=False)

    def __str__(self):
        return "{}".format(self.player.player_name[:25])


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
