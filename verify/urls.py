from django.urls import include, path
from . import views
# from django_filters.views import FilterView
# from .filters import PlayerFilter

app_name = "verify"
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    path('', views.VerifyListView.as_view(), name='verify'),
    path('verify/create', views.VerifyCreateView.as_view(), name='create'),
    path('verify/<int:pk>/verify', views.VerifyUpdateView.as_view(), name='update'),
    path('verify/<int:pk>/update', views.UpdateView.as_view(), name='update_verify'),
    path('verify/<int:pk>/delete', views.VerifyDeleteView.as_view(), name='delete'),
        
 ]