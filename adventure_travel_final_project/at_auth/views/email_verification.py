from django.shortcuts import redirect, render
from django.views import generic as views
from adventure_travel_final_project.at_auth.models import AdventureTravelUser
from adventure_travel_final_project.common.emails import send_verification_email
from adventure_travel_final_project.common.tokens import activation_token


class VerifyEmailRegisterView(views.TemplateView):
    template_name = 'auth/email_confirmation/confirm_email_initial.html'


def user_not_verified(request, pk):
    user = AdventureTravelUser.objects.get(pk=pk)
    context = {
        'user': user,
    }

    return render(request, 'auth/email_confirmation/user_not_verified.html', context)


def verify_email_login_view(request, pk):
    user = AdventureTravelUser.objects.get(pk=pk)
    template = 'auth/email_confirmation/confirm_email_additional.html'
    context = {
        'user': user,
        'domain': 'http://127.0.0.1:8000',
        'token': activation_token.make_token(user),
    }
    send_verification_email(user.email, context)

    return render(request, template)


def activate_email_view(request, pk, token):
    template = 'auth/email_confirmation/confirm_email_error.html'
    try:
        user = AdventureTravelUser.objects.get(pk=pk)
    except:
        message = 'This user does not exist'
        return validation_error_view(request, template, message)

    if user and activation_token.check_token(user, token):
        user.is_verified = True
        user.save()
        return redirect('login')
    else:
        message = 'Activation link is not valid'
        return validation_error_view(request, template, message)


def validation_error_view(request, template, message):
    context = {
        'message': message
    }

    return render(request, template, context)
