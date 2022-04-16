from django.contrib.auth import views as auth_views, login
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.views import generic as views

from adventure_travel_final_project.at_auth.forms.auth import RegisterForm, LoginForm
from adventure_travel_final_project.at_auth.models import AdventureTravelUser


class UserRegisterView(views.CreateView):
    template_name = 'auth/register.html'
    model = AdventureTravelUser
    form_class = RegisterForm
    success_url = reverse_lazy('verify email initial')


class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        user = form.get_user()
        if user.is_verified:
            login(self.request, user)
            return redirect('home')
        else:
            return redirect('verify email additional', user.id)


class UserLogoutView(auth_views.LogoutView):
    template_name = 'web/home.html'
    next_page = 'home'


class UserRequireLoginView(views.TemplateView):
    pass
