import os

import pytest
from django.core.files.base import ContentFile
from django.urls import reverse
from images.models import Image
from images.tests.helpers import temp_file
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_image_is_saved_with_thumbnail(api_client: APIClient):
    # create
    r = api_client.post(reverse("images-list"), data={"files": ContentFile(temp_file().read(), name="a.jpg")})
    assert r.status_code == 201, r.content
    img: Image = Image.objects.last()
    assert os.path.exists(img.file.path)
    assert os.path.exists(img.file.thumbnail.path)


@pytest.mark.django_db
def test_image_in_fs_is_deleted(api_client: APIClient):
    file = temp_file().read()
    img: Image = Image.objects.create(file=ContentFile(file, name="a.jpg"), extension="jpg", size=len(file))
    # delete
    r = api_client.delete(reverse("images-detail", kwargs={"pk": img.id}))
    assert r.status_code == 204
    assert not os.path.exists(img.file.path)
    assert not os.path.exists(img.file.thumbnail.path)
