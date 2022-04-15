from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_verification_email(user_email, context):
    subject = 'Verify Your Email Adress'
    message = render_to_string('auth/email_confirmation/confirm_email_message.html', context)
    sender_email = 'adventure.travel.app.team@gmail.com'
    return send_mail(subject, message, sender_email, [user_email])
