from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from adventure_travel_final_project.at_web.forms import ContactForm
from adventure_travel_final_project.at_web.models import AdventureTravelContactForm


class HomeView(views.TemplateView):
    template_name = 'web/home.html'


class AboutView(views.TemplateView):
    template_name = 'web/about.html'


class ContactFormView(views.CreateView):
    template_name = 'contact/contact_form.html'
    model = AdventureTravelContactForm
    form_class = ContactForm
    success_url = reverse_lazy('submit contact')


class SubmitContactFormView(views.TemplateView):
    template_name = 'contact/submit_contact_form.html'


def handler404(request, exception):
    context = {}
    response = render(request, "web/errors/404.html", context=context)
    response.status_code = 404
    return response


def handler500(request):
    context = {}
    response = render(request, "web/errors/500.html", context=context)
    response.status_code = 500
    return response
