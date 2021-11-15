import datetime
from django.test import TestCase
from .models import Hackathon, Workshop
from django.core.exceptions import ValidationError


# Create your tests here.
class HackathonModelTests(TestCase):
    def test_start_has_to_be_before_end(self):
        """
            start has to be before end when creating a hackathon
        """
        end = datetime.datetime(2020, 5, 17)
        start = datetime.datetime(2020, 5, 15)
        instance = Hackathon(start=end, end=start)
        self.assertRaises(ValidationError, instance.clean)
class WorkshopModelTests(TestCase):
    def test_start_has_to_be_before_end(self):
        """
            start has to be before end when creating a workshop
        """
        end = datetime.datetime(2020, 5, 17)
        start = datetime.datetime(2020, 5, 15)
        instance = Workshop(start=end, end=start)
        self.assertRaises(ValidationError, instance.clean)
