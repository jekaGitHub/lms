from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
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


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='user@example.com', password="12345")

        self.course = Course.objects.create(name="Тест", description="Новое тестовое описание", owner=self.user)
        self.lesson = Lesson.objects.create(name="Урок для теста", course=self.course,
                                            description="Тестовое описание для урока", url="https://youtube.com",
                                            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        """Тестирование вывода одного урока."""
        url = reverse("materials:lessons-retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("name"), self.lesson.name
        )

    def test_lesson_create(self):
        """Тестирование создания урока."""
        url = reverse("materials:lessons-create")
        data = {
            "name": "Экспериментальный"
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    # def test_lesson_update(self):
    #     """Тестирование обновления урока."""
    #     url = reverse("materials:lessons-update", args=(self.lesson.pk,))
    #     data = {
    #         "name": "Обновлённый"
    #     }
    #     response = self.client.patch(url, data)
    #     data = response.json()
    #
    #     self.assertEqual(
    #         response.status_code, status.HTTP_200_OK
    #     )
    #
    #     self.assertEqual(
    #         data.get("name"), "Обновлённый"
    #     )

    # def test_lesson_delete(self):
    #     """Тестирование удаления урока."""
    #     url = reverse("materials:lessons-delete", args=(self.lesson.pk,))
    #     response = self.client.delete(url)
    #
    #     self.assertEqual(
    #         response.status_code, status.HTTP_204_NO_CONTENT
    #     )
    #
    #     self.assertEqual(
    #         Lesson.objects.all().count(), 0
    #     )

    def test_lesson_list(self):
        """Тестирование вывода списка уроков."""
        url = reverse("materials:lessons-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "image": None,
                    "url": 'https://youtube.com',
                    "course": self.course.pk,
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
