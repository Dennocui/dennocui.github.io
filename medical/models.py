from django.db import models
from datetime import datetime, date
import datetime
from players.models import Player


class Injury(models.Model):
    MINIMAL = '1'
    MILD = '2'
    MODERATE = '3'
    SEVERE = '4'

    INJURY_SEVERITY = [
        (MINIMAL, 'Minimal'),
        (MILD, 'Mild'),
        (MODERATE, 'Moderate'),
        (SEVERE, 'Severe'),
    ]

    injury_serverity = models.CharField('Injury Serverity', max_length=2, choices=INJURY_SEVERITY, default=MINIMAL,)
    injury_type = models.CharField('Injury Type', max_length=225)
    notes = models.TextField('Notes', null=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{}".format(self.injury_type[:25])


class MedicalReport(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    injury = models.ForeignKey(Injury, on_delete=models.CASCADE, null=True)
    injury_date = models.DateField()
    injury_comments = models.CharField(max_length=255, null=True)
    recovery_date = models.DateField()
    conditioning_notes = models.CharField(max_length=225, null=True)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{}".format(self.player.player_name[:25])

    def days_left(self):
        today = date.today()
        recovery = self.recovery_date
        days = recovery - today
        
        return days 