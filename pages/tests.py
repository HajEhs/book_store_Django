from django.test import TestCase
from django.urls import reverse

class TestPages(TestCase):
    def test_home_page_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEquals(response.status_code, 200)

    def test_home_page_by_url(self):
        response = self.client.get("/home/")
        self.assertEquals(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Home Page")

    def test_home_page_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home_page.html")
