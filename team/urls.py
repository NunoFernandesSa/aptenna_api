from django.urls import path

from . import views

app_name = 'team'

urlpatterns = [
    path('/', views.getTeam, name='all_team'),
    path('/<str:name>/', views.getTeamByName, name='team')
]
