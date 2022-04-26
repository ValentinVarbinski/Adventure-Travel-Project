from django.core.exceptions import ValidationError

from tests.test_cases import AdventureTravelTestCases


class BlogAuthorModelTests(AdventureTravelTestCases):
    def test_blog_author_model_first_name_contain_non_english_letters__expect_exception(self):
        self.blog_author.first_name = 'Вальо'

        with self.assertRaises(ValidationError) as context:
            self.blog_author.full_clean()
            self.blog_author.save()

        self.assertIsNotNone(context.exception)

    def test_blog_author_model_last_name_contain_non_english_letters__expect_exception(self):
        self.blog_author.last_name = 'Върбински'

        with self.assertRaises(ValidationError) as context:
            self.blog_author.full_clean()
            self.blog_author.save()

        self.assertIsNotNone(context.exception)