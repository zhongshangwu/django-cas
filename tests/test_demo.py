"""A simple demo testcase."""
from django.contrib.auth.models import AnonymousUser
from django.test import Client
from django.test import RequestFactory
from django.test import TestCase
from django.urls import reverse


class DemoTestCase(TestCase):
    """Demo testcase."""

    def setUp(self):
        self.factory = RequestFactory()

    def test_ok(self):
        request = self.factory.get('/')
        request.user = AnonymousUser()

        response = Client().get(reverse("demo"))
        self.assertEqual(response.status_code, 200)
