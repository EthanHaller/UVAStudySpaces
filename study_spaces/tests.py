from django.test import TestCase
from study_spaces.models import *
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from allauth.socialaccount.models import SocialApp, SocialAccount
import os


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

class NavigationBarTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='studyspace', password='studyspacepassword')
        google_app = SocialApp.objects.create(
            provider='google',
            name='Google',
            client_id= os.environ.get("CLIENT_ID"),
            secret= os.environ.get("CLIENT_SECRET"),
        )
        SocialAccount.objects.create(
            user=self.user,
            provider=google_app.provider,
            uid='test',
        )
    def test_home_link(self):
        self.client.login(username='studyspace', password='studyspacepassword')
        response = self.client.get(reverse("study_spaces:profile"))
        self.assertContains(response, 'href="/study/"')

    def test_directions_link(self):
        self.client.login(username='studyspace', password='studyspacepassword')
        response = self.client.get(reverse("study_spaces:profile"))
        self.assertContains(response, 'href="/study/directions"')

    def test_profile_link(self):
        self.client.login(username='studyspace', password='studyspacepassword')
        response = self.client.get(reverse("study_spaces:profile"))
        self.assertContains(response, 'href="/study/profile"')

    def test_submission_link(self):
        self.client.login(username='studyspace', password='studyspacepassword')
        response = self.client.get(reverse("study_spaces:profile"))
        self.assertContains(response, 'href="/study/submission"')

class GoogleMapsViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='studyspace', password='studyspacepassword')
        google_app = SocialApp.objects.create(
            provider='google',
            name='Google',
            client_id= os.environ.get("CLIENT_ID"),
            secret= os.environ.get("CLIENT_SECRET"),
        )
        SocialAccount.objects.create(
            user=self.user,
            provider=google_app.provider,
            uid='test',
        )

    def test_google_maps_page(self):
        self.client.login(username='studyspace', password='studyspacepassword')
        response = self.client.get(reverse("study_spaces:directions"))
        self.assertEqual(response.status_code, 200)


class FeatureTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='studyspace', password='studyspacepassword')
        google_app = SocialApp.objects.create(
            provider='google',
            name='Google',
            client_id= os.environ.get("CLIENT_ID"),
            secret= os.environ.get("CLIENT_SECRET"),
        )
        SocialAccount.objects.create(
            user=self.user,
            provider=google_app.provider,
            uid='test',
        )
        newModel = StudySpace.objects.create(
            name='Rice Hall',
            address="85 Engineer's Way, Charlottesville, VA 22903",
            latitude = 38.03162799401157,
            longitude = -78.51084803374002,
            approved_submission = 1,
            user_email = '',
            denial_reason = '',
            information = 'Location: Located on Engineering Way, home to the Computer Science Department',
        )

    def test_login(self):
        self.client.login(username='studyspace', password='studyspacepassword')
        response = self.client.get("/study/")
        self.assertEqual(response.status_code, 200)
    
    def test_profile(self):
        self.client.login(username='studyspace', password='studyspacepassword')
        response = self.client.get(reverse("study_spaces:profile"))
        self.assertContains(response, 'studyspace')

    def test_more_information(self):
        self.client.login(username='studyspace', password='studyspacepassword')
        context = {
            'study_space': '1',
        }
        #response = self.client.post(reverse("study_spaces:information"), data=context_data)
        #print(response.content)
        #self.assertContains(response, 'Location: Located on Engineering Way, home to the Computer Science Department')
"""    
    def test_get_directions(self):
        # still in progress
        self.client.login(username='studyspace', password='studyspacepassword')
        form_data = {
            'startinput': '568 Buckler Dr, Charlottesville, VA 22903, USA',
            'endinput' : "85 Engineer's Way, Charlottesville, VA 22903",
            'getdirectionsbutton': 'Click Me',
        }
        response = self.client.post(reverse("study_spaces:directions"), data=form_data)
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Distance: 1.7 mi')
"""