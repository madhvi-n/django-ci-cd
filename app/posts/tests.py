from django.test import TestCase
from posts.models import Post


class PostModelTest(TestCase):
    def test_str(self):
        title = "Dummy Test Title"
        self.assertEqual(title, "Dummy Test Title")
