from django.urls import include, path
from . import views

app_name = "medical"

urlpatterns = [
    path('medical/dashboard/', views.dashboard, name='dashboard'),
    # path('dashboard/data/', views.dashboard, name='summary'),

    # path('dashbord/', views.dashboard, name='summary'),

    path('', views.MedicalListView.as_view(), name='list'),
    path('medical/<int:pk>', views.MedicalDetailView.as_view(), name='medical_details'),
    path('medical/create', views.MedicalCreateView.as_view(), name='create_medical'),
    path('medical/<int:pk>/update', views.MedicalUpdateView.as_view(), name='update_medical'),
    path('medical/<int:pk>/delete', views.MedicalDeleteView.as_view(), name='delete_medical'),

    path('injuries', views.InjuryListView.as_view(), name='injuries'),
    path('injury/<int:pk>', views.InjuryDetailView.as_view(), name='injury_details'),
    path('injury/create', views.InjuryCreateView.as_view(), name='create_injury'),
    path('injury/<int:pk>/update', views.InjuryUpdateView.as_view(), name='update_injury'),
    path('injury/<int:pk>/delete', views.InjuryDeleteView.as_view(), name='delete_injury'),
]
