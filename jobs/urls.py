from django.urls import path

from . import views

app_name = 'jobs'

urlpatterns = [
    path('/', views.getJobs, name='all_books'),
]
