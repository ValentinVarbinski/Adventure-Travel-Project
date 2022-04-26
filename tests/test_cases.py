from django.test import TestCase, Client

from adventure_travel_final_project.at_auth.models import AdventureTravelUser
from adventure_travel_final_project.at_blog.models import AdventureTravelPostAuthor
from adventure_travel_final_project.at_experiences.models import AdventureTravelExperience
from adventure_travel_final_project.at_profiles.models import AdventureTravelProfile
from adventure_travel_final_project.at_web.models import AdventureTravelContactForm


class AdventureTravelTestCases(TestCase):
    USERNAME = 'valio1'
    EMAIL = 'valio@abv.bg'
    PASSWORD = '1234'

    def setUp(self):
        self.client = Client()

        self.user = AdventureTravelUser.objects.create_user(
            username=self.USERNAME,
            email=self.EMAIL,
            password=self.PASSWORD,
            is_verified=False,
        )
        self.blog_author = AdventureTravelPostAuthor(
            first_name='Valentin',
            last_name='Varbinski',
        )

        self.contact_form = AdventureTravelContactForm(
            email='valio@abv.bg',
            subject='Subject',
            message='My message'
        )

        self.experience = AdventureTravelExperience(
            title='Tour',
            description='This is a tour',
            experience_picture='picture',
            category='sightseeing tour',
            date='24.05.2022',
            price=50,
            spots=5,
        )

        self.password_change = {
            'user': 'valio',
            'old_password': '123',
            'new_password1': 'qwe',
            'new_password2': 'qwe'
        }

        self.profile = AdventureTravelProfile(
            first_name='Valentin',
            last_name='Varbinski',
            description='My description',
            country='Bulgaria',
            facebook_account='facebook',
            instagram_account='instagram',
            twitter_account='twitter',
        )
