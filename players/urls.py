from django.urls import include, path
from . import views
from django_filters.views import FilterView
from .filters import PlayerFilter

app_name = "players"

urlpatterns = [
    #path('player', views.PlayerListView.as_view(), name='player_list'),
    path('player', FilterView.as_view(filterset_class=PlayerFilter, template_name='players/player_list.html'), name='player_list'),
    path('player/<int:pk>', views.PlayerDetailView.as_view(), name='player_details'),
    path('player/create', views.PlayerCreateView.as_view(), name='create_player'),
    path('player/<int:pk>/update', views.PlayerUpdateView.as_view(), name='update_player'),
    path('player/<int:pk>/delete', views.PlayerDeleteView.as_view(), name='delete_player'),

]
