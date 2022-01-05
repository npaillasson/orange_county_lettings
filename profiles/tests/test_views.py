import pytest

from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from profiles.models import Profile

@pytest.mark.django_db
def test_view_index():
    client = Client()
    url = reverse("profiles:index")
    response = client.get(url)
    content = response.content.decode()
    assert response.status_code == 200
    assert content.find("<title>Profiles</title>") != -1

@pytest.mark.django_db
def test_view_letting():
    username_test = "test_lettings"
    client = Client()
    User.objects.create(username=username_test, email="test.user@test.live",
                        first_name="John", last_name="Doe", password="MLKJHGFDSQ")
    Profile.objects.create(user=User.objects.get(id=1), favorite_city="Paris")
    url = reverse("profiles:profile", kwargs={"username":username_test})
    response = client.get(url)
    content = response.content.decode()
    assert response.status_code == 200
    assert content.find(f"<title>{username_test}</title>") != -1