from django.urls import reverse

from tests.test_cases import AdventureTravelTestCases


class LoginViewTests(AdventureTravelTestCases):
    def test_login_view_when_user_is_not_verified__expect_redirect_to_user_not_verified(self):
        expected_url = reverse('user not verified', args=[self.user.id])
        response = self.client.post(reverse('login'), {
            'username': self.USERNAME,
            'password': self.PASSWORD,

        })

        self.assertRedirects(response, expected_url)

