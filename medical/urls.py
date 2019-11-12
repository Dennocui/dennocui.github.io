from django.urls import include, path
from . import views

app_name = "medical"

urlpatterns = [
    path('', views.MedicalListView.as_view(), name='list'),
    path('medical/<int:pk>',
         views.MedicalDetailView.as_view(), name='medical_details'),
    path('medical/create',
         views.MedicalCreateView.as_view(), name='create_medical'),
    path('medical/<int:pk>/update',
         views.MedicalUpdateView.as_view(), name='update_medical'),
    path('medical/<int:pk>/delete',
         views.MedicalDeleteView.as_view(), name='delete_medical'),
]
