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
        ('Basic Information', {
            #   'description': "Player Bio Data.",
            'fields': (('player_name', 'date_of_birth', 'phone_number', 'email'), ('address', 'address_contact'))
        }),
        ('Identity Information', {
            'fields': (('id_number', 'id_image', 'check_id'), ('birth_cert_no', 'birth_cert_pdf', 'check_cert'), ('passport', 'passport_image', 'check_passport'))
        }),
        ('More Information', {
            #   'description': "Player Bio Data.",
            'fields': (('club', 'position'), ('skills', 'about_player', 'tertiary_institution'), ('allergy', 'injury_history'))
        }),
        ('Other Information', {
            #  'classes': ('collapse',),
            'fields': (('kin', 'kin_contact'), 'image')
        }),
    )
