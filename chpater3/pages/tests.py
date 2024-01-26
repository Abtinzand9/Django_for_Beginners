from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_url_exists_correct_lacation(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code , 200)
    def test_url_avalilable_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code , 200)
    
class AboutPageTests(SimpleTestCase):
    def test_url_exists_correct_lacation(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code , 200)
    def test_url_avalilable_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code , 200)
