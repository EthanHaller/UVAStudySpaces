from django.test import TestCase
from study_spaces.models import *

# Create your tests here.

class StudySpaceTestCase(TestCase):
    def setUp(self):
        StudySpace.objects.create(name = "Rice Hall", address = "85 Engineer's Way, Charlottesville, VA 22903", latitude = 38.03163727267092, longitude = -78.51082838815206 )
        StudySpace.objects.create(name = "Thornton Stacks A-Wing", Address = "351 McCormick Rd, Charlottesville, VA 22904", latitude = 38.03332547566759, longitude = -78.50945079424223)

    #def test_values_stored_properly(self):

