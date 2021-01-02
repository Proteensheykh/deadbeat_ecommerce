import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from apps.cart import views


class TestCartView:

    def test_cart_view_is_returned(self):
        request = RequestFactory().get('cart/')
        response = views.cart(request)
        assert response.status_code == 200, 'Should return cart page(view)'