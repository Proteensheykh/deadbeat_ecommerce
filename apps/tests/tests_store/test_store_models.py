import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from apps.store.models import Category, Product

class TestCategory:

    def test_create_category(self):
        category = mixer.blend('store.Category')
        assert category.pk == 1, 'Should create assign a primary key on create'
        assert category != None, 'Should create a category instance'

    def test_object_string(self):
        category = mixer.blend('store.Category')
        assert str(category) == category.name, 'Should display name as string'

class TestProduct:

    def test_create_Product(self):
        product = mixer.blend('store.Product')
        assert product.pk == 1, 'Should create assign a primary key on create'
        assert product != None, 'Should create a product instance'

    def test_object_string(self):
        product = mixer.blend('store.Product')
        assert str(product) == product.name, 'Should display name as string'