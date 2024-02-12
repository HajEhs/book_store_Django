from django.test import TestCase
from django.urls import reverse

class SignUpPageTset(TestCase):
    def test_signup_page_by_url(self):
        response = self.client.get("/accounts/signup/")
        self.assertEquals(response.status_code, 200)

    def test_signup_page_by_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEquals(response.status_code, 200)

    def test_signup_page_template_used(self):
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, "registration/signup_page.html")
