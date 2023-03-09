from django.urls import path

from . import views

app_name = 'technologies'


urlpatterns = [
    path('/', views.getTechnologies, name='all_technologies')
]