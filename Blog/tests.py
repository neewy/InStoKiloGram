from django.test import TestCase
from django.utils import timezone

from .models import Post
from Users import models


# Create your tests here.
# python manage.py test Blog

class PublishedTest(TestCase):
    def test_post_was_published(self):
        user = models.User(name="test user", user_type="A")
        user.save()
        post = Post(text="test_text", created_date=timezone.now(), title="Test title", author=user)
        post.save()
        self.assertIsNone(post.published_date)
        post.publish()
        self.assertIsNotNone(post.published_date)
