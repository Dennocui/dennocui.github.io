# Register your models here.
from django.contrib import admin

from .models import Conditioning, TechnicalSkill, TacticleSkill, MentalSkill, PhysicalSkill, LeadershipSkill

# admin.site.register(Conditioning)


@admin.register(Conditioning)
class ConditioningAdmin(admin.ModelAdmin):
    list_display = ('player', 'chest', 'squats', 'bench')
    list_filter = ('player', 'bench', 'squats',)
    ordering = ('player',)
    search_fields = ('player',)
    fieldsets = (

        ('Select Player', {
            'fields': ('player',)
        }),

        ('Basic Information', {

            'fields': (('bench', 'squats'), ('v_jumps', 'h_jumps'), ('t_test_right', 't_test_left'), ('yoyo'))
        }),
        ('Measurements', {

            'fields': (('chest', 'bicep'), ('waist', 'hip', 'thigh'))
        }),
        ('Metre Sprints', {

            'fields': (('m10', 'm40'), ('m60'))
        }),
        ('Other Information', {

            'fields': (('suppliment_taken'), ('conditioning_notes'))
        }),
    )

admin.site.register(TechnicalSkill)
admin.site.register(TacticleSkill)
admin.site.register(MentalSkill)
admin.site.register(PhysicalSkill)
admin.site.register(LeadershipSkill)