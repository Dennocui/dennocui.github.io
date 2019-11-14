from django.urls import include, path
from . import views

app_name = "snc"

urlpatterns = [
    path('', views.ConditioningListView.as_view(), name='list'),
    path('snc/<int:pk>', views. ConditioningDetailView.as_view(), name='conditioning_details'),
    path('snc/create', views.ConditioningCreateView.as_view(), name='create_conditioning'),
    path('snc/<int:pk>/update', views.ConditioningUpdateView.as_view(), name='update_conditioning'),
    path('snc/<int:pk>/delete', views.ConditioningDeleteView.as_view(), name='delete_conditioning'),

    
    
    path('technical', views.TechnicalListView.as_view(), name='technical_list'),
    path('technical/<int:pk>', views. TechnicalDetailView.as_view(), name='technical_details'),
    path('technical/create', views.TechnicalCreateView.as_view(), name='create_technical'),
    path('technical/<int:pk>/update', views.TechnicalUpdateView.as_view(), name='update_technical'),
#     path('technical/<int:pk>/delete', views.TechnicalDeleteView.as_view(), name='delete_technical'),

     
    path('tacticle', views.TacticleListView.as_view(), name='tacticle_list'),
    path('tacticle/<int:pk>', views. TacticleDetailView.as_view(), name='tacticle_details'),
    path('tacticle/create', views.TacticleCreateView.as_view(), name='create_tacticle'),
    path('tacticle/<int:pk>/update', views.TacticleUpdateView.as_view(), name='update_tacticle'),
#     path('tacticle/<int:pk>/delete', views.TacticleDeleteView.as_view(), name='delete_tacticle'),

     
    path('mental', views.MentalListView.as_view(), name='mental_list'),
    path('mental/<int:pk>', views. MentalDetailView.as_view(), name='mental_details'),
    path('mental/create', views.MentalCreateView.as_view(), name='create_mental'),
    path('mental/<int:pk>/update', views.MentalUpdateView.as_view(), name='update_mental'),
#     path('mental/<int:pk>/delete', views.MentalDeleteView.as_view(), name='delete_mental'),

     
    path('physical', views.PhysicalListView.as_view(), name='physical_list'),
    path('physical/<int:pk>', views. PhysicalDetailView.as_view(), name='physical_details'),
    path('physical/create', views.PhysicalCreateView.as_view(), name='create_physical'),
    path('physical/<int:pk>/update', views.PhysicalUpdateView.as_view(), name='update_physical'),
#     path('physical/<int:pk>/delete', views.PhysicalDeleteView.as_view(), name='delete_physical'),

     
    path('leadership', views.LeadershipListView.as_view(), name='leadership_list'),
    path('leadership/<int:pk>', views. LeadershipDetailView.as_view(), name='leadership_details'),
    path('leadership/create', views.LeadershipCreateView.as_view(), name='create_leadership'),
    path('leadership/<int:pk>/update', views.LeadershipUpdateView.as_view(), name='update_leadership'),
#     path('leadership/<int:pk>/delete', views.LeadershipDeleteView.as_view(), name='delete_leadership'),

     
]
