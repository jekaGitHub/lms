from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course
from users.models import User


# Create your tests here.
class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='user@example.com', password="12345")

        self.course = Course.objects.create(name="Тест", description="Новое тестовое описание", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        """Тестирование вывода одного курса."""
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("name"), self.course.name
        )

    def test_course_create(self):
        """Тестирование создания курса."""
        url = reverse("materials:course-list")
        data = {
            "name": "Экспериментальный"
        }
        response = self.client.post(url, data)
        # print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        """Тестирование обновления курса."""
        url = reverse("materials:course-detail", args=(self.course.pk,))
        data = {
            "name": "Обновлённый"
        }
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("name"), "Обновлённый"
        )

    def test_course_delete(self):
        """Тестирование удаления курса."""
        url = reverse("materials:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):
        """Тестирование вывода списка курсов."""
        url = reverse("materials:course-list")
        response = self.client.get(url)
        data = response.json()
        result = {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.course.pk,
                        "lessons_count": 0,
                        "lessons_info": [],
                        "name": self.course.name,
                        "image": None,
                        "description": self.course.description,
                        "owner": self.user.pk
                    }
                ]
        }
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, result
        )
