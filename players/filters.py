from . models import Player

import django_filters


class PlayerFilter(django_filters.FilterSet):
    player_name = django_filters.CharFilter(lookup_expr='icontains')
    # date_of_birth = django_filters.NumberFilter(lookup_expr='year')

    class Meta:
        model = Player
        fields = ['player_name',  'club', 'position', ]
