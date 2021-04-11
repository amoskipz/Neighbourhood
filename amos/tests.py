from django.test import TestCase
from .models import neighbourhood
from django.contrib.auth.models import User
# Create your tests here.

class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Bomet = neighbourhood(neighbourhood='Bomet')

    def test_instance(self):
        self.assertTrue(isinstance(self.Bomet,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Bomet.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Bomet.delete_neighbourhood('Bomet')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)