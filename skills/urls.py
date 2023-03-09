from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('/', views.getSkills, name='all_skills'),
]
