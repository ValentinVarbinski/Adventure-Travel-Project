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

    def test_login_view_when_user_is_verified__expect_redirect_to_user_not_verified(self):
        self.client.login(username=self.USERNAME, password=self.PASSWORD)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web/home.html')




