from django.contrib.auth.models import AbstractUser
from django.db import models

from config import settings
from materials.models import Course, Lesson, NULLABLE


# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email")

    phone = models.CharField(
        max_length=35,
        verbose_name="Номер телефона",
        help_text="Укажите телефон",
        **NULLABLE
    )
    city = models.CharField(
        max_length=35, verbose_name="Страна", help_text="Укажите город", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatar/",
        verbose_name="Аватар",
        help_text="Загрузите аватар",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    PAYMENT_METHOD = (
        ("cash", "наличные"),
        ("transfer", "перевод на счет"),
    )

    user_payer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="Плательщик",
        help_text="Укажите плательщика"
    )
    payment_date = models.DateTimeField(
        verbose_name="Дата оплаты", help_text="Укажите дату оплаты"
    )
    course_paid = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="payments_course",
        verbose_name="Оплаченный курс",
        help_text="Укажите оплаченный курс",
        **NULLABLE
    )
    lesson_paid = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="payments_lesson",
        verbose_name="Оплаченный урок",
        help_text="Укажите оплаченный урок",
        **NULLABLE
    )
    payment_amount = models.DecimalField(
        decimal_places=2,
        max_digits=7,
        verbose_name="Сумма оплаты",
        help_text="Укажите сумму оплаты"
    )
    payment_method = models.CharField(
        choices=PAYMENT_METHOD,
        max_length=255,
        default="daily",
        verbose_name="Способ оплаты",
        help_text="Выберите способ оплаты",
        **NULLABLE
    )

    session_id = models.CharField(max_length=255, verbose_name="ID сессии", **NULLABLE)
    link_pay = models.URLField(max_length=400, verbose_name="Ссылка на оплату", **NULLABLE)

    def __str__(self):
        return f'{self.user_payer} - {self.course_paid}({self.payment_amount})'

    class Meta:
        verbose_name = "Платёж"
        verbose_name_plural = "Платежи"


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь подписки",
                             **NULLABLE,
                             help_text="Укажите пользователя подписки")
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               related_name="subscriptions",
                               verbose_name="Курс для подписки",
                               help_text="Укажите курс для подписки",
                               **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name="Активность подписки")

    def __str__(self):
        return f'{self.user} - {self.course}({self.is_active})'

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
