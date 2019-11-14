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




class TechnicalSkill(models.Model):
    WORKON = '1'
    ADEQUATE = '2'
    EXCELLENT = '3'

    SKILL_LEVEL = [
        (WORKON, 'Work On'),
        (ADEQUATE, 'Adequate'),
        (EXCELLENT, 'Excellent')
    ]


    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    catch_pass = models.CharField('Catch & Pass',max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    tackle = models.CharField('Tackles',max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    post_tackle = models.CharField('Post-tackle',max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    carry = models.CharField('Carry',max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    clean_out = models.CharField('Clean Out', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    off_load = models.CharField('Off-load', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    one_on_one = models.CharField('One on One', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    support = models.CharField('Support Play',max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    high_ball = models.CharField('High Ball', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    kicking = models.CharField('Kicking(Grubber/Punt/Chip)', max_length=15, choices=SKILL_LEVEL, null=True,)
    commment = models.TextField()

    created_at = models.DateTimeField('Date Created', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.player.player_name[:25])



class TacticleSkill(models.Model):
    WORKON = '1'
    ADEQUATE = '2'
    EXCELLENT = '3'
    

    SKILL_LEVEL = [
        (WORKON, 'Work On'),
        (ADEQUATE, 'Adequate'),
        (EXCELLENT, 'Excellent')
    ]

    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    positioning = models.CharField('Positioning', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    gameplan = models.CharField('Game Plan and Role Understanding', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    workrate = models.CharField('Workrate', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    tactical_awareness = models.CharField('Tactical awareness', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    communication  = models.CharField('Communication',max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    scrummaging = models.CharField('Scrummaging', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    throwing = models.CharField('Throwing(Hooker)', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    kicking_post = models.CharField('Kicking for Post', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    tacticle_commment = models.TextField('Commments',)

    created_at = models.DateTimeField('Date Created', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.player.player_name[:25])

class PhysicalSkill(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    body_weight = models.DecimalField('Body Weight',max_digits=5, decimal_places=2)
    bench_press = models.IntegerField('Bench Press(1RM)',)
    bent_over_row = models.IntegerField('Bent Over Row',)
    deadlift = models.IntegerField('Deadlift',)
    squats = models.IntegerField('Squarts',)
    m10 = models.DecimalField('10M Sprints', max_digits=5, decimal_places=2)
    m40 = models.DecimalField('40M Sprints',max_digits=5, decimal_places=2)
    yoyo = models.DecimalField('Yoyo', max_digits=5, decimal_places=2)
    physical_commment = models.TextField('Commments',)

    created_at = models.DateTimeField('Date Created', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return "{}".format(self.player.player_name[:25])

class MentalSkill(models.Model):
    WORKON = '1'
    ADEQUATE = '2'
    EXCELLENT = '3'

    SKILL_LEVEL = [
        (WORKON, 'Work On'),
        (ADEQUATE, 'Adequate'),
        (EXCELLENT, 'Excellent')
    ]
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    self_drive = models.CharField('Self Drive', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    readiness = models.CharField('Performance Readiness', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    focus = models.CharField('Perfomance Focus', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    review = models.CharField('Perfomance Review', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    resilience = models.CharField('Resilience', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    work_ethic = models.CharField('Work Ethic', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    mental_commment = models.TextField('Commments',)

    created_at = models.DateTimeField('Date Created', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.player.player_name[:25])


class LeadershipSkill(models.Model):
    WORKON = '1'
    ADEQUATE = '2'
    EXCELLENT = '3'

    SKILL_LEVEL = [
        (WORKON, 'Work On'),
        (ADEQUATE, 'Adequate'),
        (EXCELLENT, 'Excellent')
    ]
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    self_awareness = models.CharField('Self Awareness', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    other_awareness =models.CharField('Awareness of others', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    self_reliance = models.CharField('Self Reliance', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    life_balance = models.CharField('Life balance', max_length=15, choices=SKILL_LEVEL, default=WORKON,)
    leadership_commment = models.TextField('Commments',)

    created_at = models.DateTimeField('Date Created', auto_now=True, auto_now_add=False)
    last_modified = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{}".format(self.player.player_name[:25])