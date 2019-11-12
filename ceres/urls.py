from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(),
         name='admin_password_reset',),
    path('admin/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(), name='password_reset_done',),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm',),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete',),

    path('', views.signin, name='signin'),

    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('main/', include('main.urls', namespace='main')),
    path('', include('players.urls', namespace='players')),
    path('medical/', include('medical.urls', namespace='medical')),
    path('snc/', include('snc.urls', namespace='snc')),
    path('events/', include('events.urls', namespace='events')),

]


if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
