from django.db import models

from users.models import NULLABLE


# Create your models here.
class Course(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    image = models.ImageField(
        upload_to="preview/course",
        verbose_name="Превью",
        help_text="Загрузите фото",
        **NULLABLE,
    )
    description = models.TextField(
        verbose_name="Описание курса", help_text="Укажите описание курса", **NULLABLE
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(
        max_length=150,
        help_text="Укажите название урока",
        verbose_name="Название урока",
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        related_name="lessons",
        help_text="Выберите курс",
        verbose_name="Курс",
        **NULLABLE,
    )

    description = models.TextField(
        verbose_name="Описание урока", help_text="Укажите описание урока", **NULLABLE
    )
    image = models.ImageField(
        upload_to="preview/lesson",
        verbose_name="Превью",
        help_text="Загрузите фото",
        **NULLABLE,
    )
    url = models.URLField(
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео урока",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
