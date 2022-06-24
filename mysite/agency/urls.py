from django.urls import path
from . import views


app_name = 'agency'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('genres/', views.genres, name='genres'),
    path('festivals/', views.festivals, name='festivals'),
    path('tickets/', views.tickets, name='tickets'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
    # path('', views.index, name='index'),
] 