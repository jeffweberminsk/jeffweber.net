from django.test import TestCase

# Create your tests here.
from datetime import datetime, timedelta, timezone

from django.test import TestCase

from jeffwebersite.website.models import Category


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test')

    def test_category_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 1000)
