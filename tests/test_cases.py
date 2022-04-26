from django.test import TestCase, Client

from adventure_travel_final_project.at_auth.models import AdventureTravelUser


class AdventureTravelTestCases(TestCase):
    username = 'valio1'
    email = 'valio@abv.bg'
    password = '1234'

    def setUp(self):
        self.client = Client()
        self.user = AdventureTravelUser.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
            is_verified=False,
        )
