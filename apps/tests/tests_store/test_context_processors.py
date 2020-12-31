import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from apps.store import context_processors as cp

class TestContextProcessor:

    def test_category_processor(self):

        request = RequestFactory().get('')
        assert 'menu_categories' in cp.menu_categories(request).keys(), 'Should return object with Category list'