from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('get_user_info/', views.get_user_info, name='get_user_info'),
    path('update_user_info/', views.update_user_info, name='update_user_info'),
    path('add_passenger/', views.add_passenger, name='add_passenger'),
    path('remove_passenger/', views.remove_passenger, name='remove_passenger'),
    path('update_passenger/', views.update_passenger, name='update_passenger'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('logoff/', views.logoff, name='logoff'),
    path('recharge/', views.recharge, name='recharge'),
    path('get_user_list/', views.get_user_list, name='get_user_list'),
    path('add_user/', views.add_user, name='add_user'),
    path('update_user_info_system_admin/', views.update_user_info_system_admin, name='update_user_info_system_admin'),
    path('remove_user/', views.remove_user, name='remove_user'),
    path('get_admin_info/', views.get_admin_info),
    path('get_passenger_list/', views.get_passenger_list)
]