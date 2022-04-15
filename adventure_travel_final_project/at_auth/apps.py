from django.apps import AppConfig


class AtAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adventure_travel_final_project.at_auth'



#
# class ActivityAppConfig(AppConfig):
#     name = 'adventure_travel_final_project'
#
#     def ready(self):
#         import adventure_travel_final_project.common.signals
