from django.urls import path

from .import views

app_name = 'accounts'

urlpatterns = [

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('create_user', views.SignUpView.as_view(), name='create_user'),
    path('users_list', views.UserListView.as_view(), name='users_list'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user_details'),
    path('user/<int:pk>/update',
         views.UserUpdateView.as_view(), name='update_user'),
    path('user/<int:pk>/delete',
         views.UserDeleteView.as_view(), name='delete_user'),
]
