from django.urls import path

from adventure_travel_final_project.at_web.views import HomeView, AboutView, ContactFormView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
