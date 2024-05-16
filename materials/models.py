import datetime

from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


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

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Владелец курса", help_text="Укажите владельца курса")

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

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Владелец урока",
                              help_text="Укажите владельца урока")

    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         old_lesson = Lesson.objects.get(pk=self.pk)
    #         now = datetime.datetime.now()
    #         if (now - old_lesson.updated).seconds > 60 * 60 * 4:
                # рассылать пользователям сообщение о том, что урок обновился

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
