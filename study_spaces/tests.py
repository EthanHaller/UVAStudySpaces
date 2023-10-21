from django.test import TestCase
from study_spaces.models import *
from django.urls import reverse

# Create your tests here.

class StudySpaceTestCase(TestCase):
    def setUp(self):
        StudySpace.objects.create(name = "Rice Hall", address = "85 Engineer's Way, Charlottesville, VA 22903", latitude = 38.03163727267092, longitude = -78.51082838815206 )
        StudySpace.objects.create(name = "Thornton Stacks A-Wing", Address = "351 McCormick Rd, Charlottesville, VA 22904", latitude = 38.03332547566759, longitude = -78.50945079424223)
    def test_model_string(self):
        rice_hall = StudySpace.objects.get(name="Rice Hall")
        thornton = StudySpace.objects.get(name="Thornton Stacks A-Wing")
        self.assertEqual(rice_hall.get_sentence, "Rice Hall is located at 85 Engineer's Way, Charlottesville, VA 22903")
        self.assertEqual(thornton.get_sentence, "Thornton Stacks A-Wing is located at 351 McCormick Rd, Charlottesville, VA 22904")

class StudySpaceViewTest(TestCase):
    def test_redirect(self):

        #reference: https://docs.djangoproject.com/en/4.2/intro/tutorial05/

        response = self.client.get(reverse("map"))
        response2 = self.client.get(reverse("study_spaces:route"))
        response3 = self.client.get(reverse("study_spaces:profile"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response2.status_code, 302)
        self.assertEqual(response3.status_code, 302)
