from django.test import TestCase
from . import models

class SimpleTest(TestCase):
    def test_first_object_in_db(self):
        obj1 = models.SimpleModel.objects.first()
        self.assertEqual(obj1.just_text, 'text_1')
    def test_second_object_in_db(self):
        obj2 = models.SimpleModel.objects.get(pk=2)
        self.assertEqual(obj2.just_text, 'text_2')

    # def test_3_object_in_db(self):
    #     obj2 = models.SimpleModel.objects.get(pk=3)
    #     self.assertEqual(obj2.just_text, 'text_3')