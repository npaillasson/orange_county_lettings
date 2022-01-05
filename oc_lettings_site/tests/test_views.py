import pytest

from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_view_index():
    client = Client()
    url = reverse("index")
    response = client.get(url)
    content = response.content.decode()
    assert response.status_code == 200
    assert content.find("<title>Holiday Homes</title>") != -1
