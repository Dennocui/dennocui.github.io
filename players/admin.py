from django.contrib import admin
from .models import Player
# Register your models here.


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    # fields = ('player_name','email','date_of_birth', 'address','phone_number','kin','kin_contact','passport','address_contact','id_number','image');
    list_display = ('player_name', 'email', 'age', 'address', 'phone_number')
    list_filter = ('address',)
    ordering = ('player_name',)
    search_fields = ('player_name', 'address')
    fieldsets = (
        ('Personal Information', {
            #   'description': "Player Bio Data.",
            'fields': (('player_name', 'date_of_birth', 'phone_number', 'email'), ('address'), ('kin', 'kin_contact'))
        }),

        ('Player Details', {
            #   'description': "Player Bio Data.",
            'fields': (('club', 'position'), ('high_school', 'tertiary_institution'), ('allergy', 'injury_history','about_player'))
        }),

        ('Other Information', {
            #  'classes': ('collapse',),
            'fields': ('image',)
        }),
    )

#