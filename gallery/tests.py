from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Category, Photo
import os


class TestCategories(TestCase):
    def test_category_name(self):
        category = Category.objects.create(title="Nature")

        self.assertEqual(category.title, "Nature")


class TestPhoto(TestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(title="Nature")

    def test_upload_photo(self):
        self.photo = Photo.objects.create(
            title="Test photo",
            category=self.category,
            image=SimpleUploadedFile(
                name="IMG_1098.JPG",
                content=open("E:/Photos/CIW/IMG_1098.JPG", "rb").read(),
                content_type="image/jpg"
            ),
            comment="Testing photo upload"
        )

        self.assertTrue(os.path.exists(self.photo.image.path))