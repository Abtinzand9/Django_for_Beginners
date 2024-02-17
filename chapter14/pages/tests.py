from django.test import TestCase ,SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_url_exsist_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code , 200)

    def test_hompage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code , 200)
        self.assertTemplateUsed(response , 'home.html')
        self.assertContains(response , 'Home')
        