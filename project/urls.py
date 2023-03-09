from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('aptenna_admin/', admin.site.urls),
                  path('api/jobs', include('jobs.urls')),
                  path('api/services', include('services.urls')),
                  path('api/skills', include('skills.urls')),
                  path('api/team', include('team.urls')),
                  path('api/technologies', include('technologies.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
