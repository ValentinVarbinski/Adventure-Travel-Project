from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'web/home.html'


class AboutView(TemplateView):
    template_name = 'web/about.html'


class ContactFormView(TemplateView):
    template_name = 'contact/contact_form.html'
