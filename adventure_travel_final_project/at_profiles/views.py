from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from adventure_travel_final_project.at_experiences.models import AdventureTravelExperience, AdventureTravelRegistration
from adventure_travel_final_project.at_profiles.forms import UserProfileForm, ChangePasswordForm
from adventure_travel_final_project.at_profiles.models import AdventureTravelProfile


class ProfileView(auth_mixins.LoginRequiredMixin, views.DetailView):
    model = AdventureTravelProfile
    context_object_name = 'profile'
    template_name = 'profiles/profile_details.html'

    def get_queryset(self):
        return AdventureTravelProfile.objects.filter(user_id=self.request.user.id)


@login_required()
def edit_profile_view(request, pk):
    profile = AdventureTravelProfile.objects.get(pk=pk)
    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', pk)

    context = {
        'form': form,
    }
    return render(request, 'profiles/edit_profile.html', context)


class ChangePasswordView(auth_mixins.LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'profiles/change_password_profile.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('home')


class MyExperiencesView(auth_mixins.LoginRequiredMixin, views.ListView):
    template_name = 'experiences/my_experiences.html'
    context_object_name = 'experiences'
    model = AdventureTravelRegistration

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        experiences = list(AdventureTravelRegistration.objects.filter(client_id=self.request.user))

        context.update(
            {
                'experiences': experiences,
            }
        )

        return context


class ExperienceCancelView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'experiences/adventuretravelregistration_confirm_delete.html'
    model = AdventureTravelRegistration
    success_url = reverse_lazy('home')
