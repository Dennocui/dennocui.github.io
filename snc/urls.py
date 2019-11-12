from django.urls import include, path
from . import views

app_name = "snc"

urlpatterns = [
    path('', views.ConditioningListView.as_view(), name='list'),
    path('snc/<int:pk>',
         views. ConditioningDetailView.as_view(), name='conditioning_details'),
    path('snc/create',
         views.ConditioninglCreateView.as_view(), name='create_conditioning'),
    path('snc/<int:pk>/update',
         views.ConditioningUpdateView.as_view(), name='update_conditioning'),
    path('snc/<int:pk>/delete',
         views.ConditioningDeleteView.as_view(), name='delete_conditioning'),
]
