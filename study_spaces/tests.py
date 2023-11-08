from django.test import TestCase
from study_spaces.models import *
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.

class StudySpaceTestCase(TestCase):
    def setUp(self):
        StudySpace.objects.create(name="Rice Hall", address="85 Engineer's Way, Charlottesville, VA 22903",
                                  latitude=38.03163727267092, longitude=-78.51082838815206)
        StudySpace.objects.create(name="Thornton Stacks A-Wing", address="351 McCormick Rd, Charlottesville, VA 22904",
                                  latitude=38.03332547566759, longitude=-78.50945079424223)

    def test_model_string(self):
        rice_hall = StudySpace.objects.get(name="Rice Hall")
        thornton = StudySpace.objects.get(name="Thornton Stacks A-Wing")
        rice_sentence = rice_hall.get_sentence()
        thornton_sentence = thornton.get_sentence()
        self.assertEqual(rice_sentence, "Rice Hall is located at 85 Engineer's Way, Charlottesville, VA 22903.")
        self.assertEqual(thornton_sentence,
                         "Thornton Stacks A-Wing is located at 351 McCormick Rd, Charlottesville, VA 22904.")


class StudySpaceViewTest(TestCase):
    def test_redirect(self):
        # reference: https://docs.djangoproject.com/en/4.2/intro/tutorial05/

        response = self.client.get(reverse("study_spaces:directions"))
        response2 = self.client.get(reverse("study_spaces:profile"))
        response3 = self.client.get(reverse("study_spaces:submission"))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(response3.status_code, 302)


"""
class NavigationBarTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_home_link(self):
        response = self.client.get(reverse("study_spaces:profile"))
        self.assertContains(response, 'href="/study/"')

    def test_directions_link(self):
        response = self.client.get(reverse("study_spaces:profile"))
        self.assertContains(response, 'href="/study/directions"')

    def test_profile_link(self):
        response = self.client.get(reverse("study_spaces:profile"))
        self.assertContains(response, 'href="/study/profile"')

    def test_submission_link(self):
        response = self.client.get(reverse("study_spaces:profile"))
        self.assertContains(response, 'href="/study/submission"')


class GoogleMapsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_google_maps_page(self):
        response = self.client.get(reverse("study_spaces:directions"))
        self.assertEqual(response.status_code, 200)

    def test_google_maps_init(self):
        response = self.client.get(reverse("study_spaces:directions"))
        self.assertContains(response, "initMap")

    def test_google_maps_api(self):
        response = self.client.get(reverse("study_spaces:directions"))
        self.assertContains(response, "maps.googleapis.com/maps/api/js?key=")
"""
