from django.urls import path
from . import views


app_name = 'agency'

urlpatterns = [
    path('', views.index, name='index'),
    # path('start/', views.mainpage, name='mainpage'),
    path('profile/', views.profile, name='profile'),
    path('profile/delete', views.profile_delete, name='profile_delete'),
    path('profile/delete/result', views.profile_delete_result, name='profile_delete_result'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/edit/result', views.profile_edit_result, name='profile_edit_result'),
    path('genres/', views.genres, name='genres'),
    path('festivals/', views.festivals, name='festivals'),
    path('tickets/', views.tickets, name='tickets'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
] 