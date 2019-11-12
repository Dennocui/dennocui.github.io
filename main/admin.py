from django.contrib import admin

from .models import Club, Position, HighSchool, ClubAdmin


@admin.register(ClubAdmin)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('user', 'club', 'created_at', 'last_modified')
    list_filter = ('user', 'club',)
    ordering = ('club',)
    search_fields = ('user', 'club')
    fieldsets = (
        ('Information', {
            #   'description': "Player Bio Data.",
            'fields': ('user', 'club')
        }),

    )


admin.site.register(Position)
admin.site.register(HighSchool)
admin.site.register(Club)
