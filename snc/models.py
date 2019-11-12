from django.db import models
from django.utils import timezone

from players.models import Player


class Conditioning(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    bench = models.IntegerField()
    squats = models.IntegerField()
    v_jumps = models.DecimalField(max_digits=5, decimal_places=2)
    h_jumps = models.DecimalField(max_digits=5, decimal_places=2)
    yoyo = models.DecimalField(max_digits=5, decimal_places=2)
    t_test_right = models.DecimalField(max_digits=5, decimal_places=2)
    t_test_left = models.DecimalField(max_digits=5, decimal_places=2)
    chest = models.DecimalField(max_digits=5, decimal_places=2)
    bicep = models.DecimalField(max_digits=5, decimal_places=2)
    waist = models.DecimalField(max_digits=5, decimal_places=2)
    hip = models.DecimalField(max_digits=5, decimal_places=2)
    thigh = models.DecimalField(max_digits=5, decimal_places=2)
    m10 = models.DecimalField(max_digits=5, decimal_places=2)
    m40 = models.DecimalField(max_digits=5, decimal_places=2)
    m60 = models.DecimalField(max_digits=5, decimal_places=2)
    suppliment_taken = models.CharField(max_length=225, null=True)
    conditioning_notes = models.CharField(max_length=225, null=True)

    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{}".format(self.player.player_name[:25])
