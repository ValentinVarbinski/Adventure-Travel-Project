from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from adventure_travel_final_project.at_experiences.models import AdventureTravelExperience, AdventureTravelRegistration


def show_experiences_view(request):
    experiences = AdventureTravelExperience.objects.all().order_by('date')
    context = {
        'experiences': experiences,
    }
    return render(request, 'experiences/experiences.html', context)


@login_required(login_url='require login')
def register_for_experience_view(request, pk):
    experience = AdventureTravelExperience.objects.get(pk=pk)
    experience_register = AdventureTravelRegistration(
        experience=experience,
        client=request.user,
    )

    if AdventureTravelRegistration.objects.filter(experience=experience, client=request.user).exists():
        return render(request, 'experiences/register_already.html')
    else:
        experience_register.save()
        exp = AdventureTravelExperience.objects.get(pk=pk)
        exp.spots -= 1
        exp.save()
        return render(request, 'experiences/register_for_experience.html')



