from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver
from adventure_travel_final_project.at_auth.models import AdventureTravelUser
from adventure_travel_final_project.at_profiles.models import AdventureTravelProfile
from adventure_travel_final_project.common.emails import send_verification_email
from adventure_travel_final_project.common.tokens import activation_token

User = get_user_model()


@receiver(signals.post_save, sender=User)
def new_user_register(sender, instance, created, **kwargs):
    user = instance
    context = {
        'user': user,
        'domain': 'http://127.0.0.1:8000',
        'token': activation_token.make_token(user)
    }

    if created:
        send_verification_email(user.email, context)
        profile = AdventureTravelProfile(
            user=instance,
        )
        profile.save()
