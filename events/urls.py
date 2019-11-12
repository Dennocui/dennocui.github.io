from django.urls import include, path
from . import views

app_name = "events"

urlpatterns = [

    path('calendar', views.calendar, name='calendar'),
    path('add_event', views.add_event, name='add_event'),
    path('update', views.update, name='update'),
    path('remove', views.remove, name='remove'),

    #     path('calender', views.calender, name='calender'),
    #     path('calendar', views.CalendarView.as_view(), name='calendar'),  # here
    #     path('event/new/', views.event, name='event_new'),
    #     path('event/edit/<int:event_id>/', views.event, name='event_edit'),



    #     path('add_event', views.add_event, name='add_event'),
    #     path('update', views.update, name='update'),
    #     path('remove', views.remove, name='remove'),
]
