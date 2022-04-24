from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('adventure_travel_final_project.at_web.urls')),
                  path('auth/', include('adventure_travel_final_project.at_auth.urls')),
                  path('profiles/', include('adventure_travel_final_project.at_profiles.urls')),
                  path('experience/', include('adventure_travel_final_project.at_experiences.urls')),
                  path('blog/', include('adventure_travel_final_project.at_blog.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
