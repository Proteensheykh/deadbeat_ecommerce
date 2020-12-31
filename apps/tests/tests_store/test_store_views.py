import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from apps.store.models import Product, Category
from apps.store import views

class TestProductDetailView:

    def test_product_detail_view(self):
        product = mixer.blend('store.Product')
        category = mixer.blend('store.Category')
        url = category.slug + '/' + product.slug + '/'
        request = RequestFactory().get(url)
        response = views.product_detail(request, category.slug, product.slug)
        assert response.status_code == 200, 'Should return product details'

class TestCategoryDetailView:

    def test_category_detail_view(self):
        category = mixer.blend('store.Category')
        url = '/' + category.slug
        request = RequestFactory().get(url)
        response = views.category_detail(request, category.slug)
        assert response.status_code == 200, 'Should return category details'
        
