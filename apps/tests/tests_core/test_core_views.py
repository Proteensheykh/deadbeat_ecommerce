import pytest
from django.test import RequestFactory, Client
pytestmark = pytest.mark.django_db

from apps.core import views

class TestFrontPageView:

    def test_product_list_display(self):
        request = RequestFactory().get('/')
        response = views.frontpage(request)
        assert response.status_code == 200, 'Should return list of products'

class TestContactPageView:

    def test_contact_view(self):
        request = RequestFactory().get('/contact')
        response = views.contact(request)
        assert response.status_code == 200, 'Should display contact info'

class TestAboutPageView:

    def test_about_view(self):
        request = RequestFactory().get('/about')
        response = views.about(request)
        assert response.status_code == 200, 'Should display about info'  

