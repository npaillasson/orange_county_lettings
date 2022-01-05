import pytest

from django.test import Client
from django.urls import reverse, resolve
from lettings.models import Address, Letting

@pytest.mark.django_db
def test_view_index():
    client = Client()
    url = reverse("lettings:index")
   #Address.objects.create(number=12, street="avenue marceau", city="Romainville", state="az",
   #                        zip_code=333, country_iso_code = "abf")
    response = client.get(url)
    content = response.content.decode()
    assert response.status_code == 200
    assert content.find("<title>Lettings</title>") != -1

@pytest.mark.django_db
def test_view_letting():
    title_test = "test_lettings"
    client = Client()
    Address.objects.create(number=12, street="avenue marceau", city="Romainville",
                           state="az", zip_code=333, country_iso_code="abf")
    Letting.objects.create(title=title_test, address=Address.objects.get(id=1))
    url = reverse("lettings:letting", kwargs={"letting_id":1})
    response = client.get(url)
    content = response.content.decode()
    assert response.status_code == 200
    assert content.find(f"<title>{title_test}</title>") != -1