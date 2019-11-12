from django.contrib import admin

# Register your models here.


from .models import MedicalReport, Injury

admin.site.register(Injury)
admin.site.register(MedicalReport)
# @admin.register(MedicalReport)
# class MedicalReportAdmin(admin.ModelAdmin):
#     list_display = ('player', 'injury_type', 'injury_date', 'injury_comments',
#                     'recovery_date', 'conditioning_notes', 'created_at')
#     list_filter = ('injury_type', 'injury_date',
#                    'recovery_date', 'created_at', 'player',)
#     ordering = ('created_at', 'injury_type', 'recovery_date',)
#     search_fields = ('player', 'injury_type')
#     fieldsets = (
#         ('Basic Information', {
#             #   'description': "Player Bio Data.",
#             'fields': (('player'), ('injury_type', 'injury_date', 'injury_comments', 'recovery_date'), ('conditioning_notes')
#                        )}),


#     )
