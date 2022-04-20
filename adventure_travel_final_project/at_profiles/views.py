from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

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
