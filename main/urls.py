from django.urls import include, path
from . import views
from django_filters.views import FilterView
# from .filters import PlayerFilter

app_name = "main"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('admin/create', views.ClubAdminCreateView.as_view(), name='club_admin'),
    path('club', views.ClubListView.as_view(), name='club_list'),
    path('club/<int:pk>', views.ClubDetailView.as_view(), name='club_details'),
    path('club/create', views.ClubCreateView.as_view(), name='create_club'),
    path('club/<int:pk>/update', views.ClubUpdateView.as_view(), name='update_club'),
    path('club/<int:pk>/delete', views.ClubDeleteView.as_view(), name='delete_club'),

    #     path('referee', views.RefereeListView.as_view(), name='referee_list'),
    #     path('referee/<int:pk>', views.RefereeDetailView.as_view(), name='referee_details'),
    #     path('referee/create', views.RefereeCreateView.as_view(), name='create_referee'),
    #     path('referee/<int:pk>/update', views.RefereeUpdateView.as_view(), name='update_referee'),
    #     path('referee/<int:pk>/delete', views.RefereeDeleteView.as_view(), name='delete_referee'),

]
