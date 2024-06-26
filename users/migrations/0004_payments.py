# Generated by Django 4.2.2 on 2024-04-20 15:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0001_initial"),
        ("users", "0003_alter_user_avatar_alter_user_city_alter_user_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_date",
                    models.DateTimeField(
                        help_text="Укажите дату оплаты", verbose_name="Дата оплаты"
                    ),
                ),
                (
                    "payment_amount",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Укажите сумму оплаты",
                        max_digits=7,
                        verbose_name="Сумма оплаты",
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        blank=True,
                        choices=[("cash", "наличные"), ("transfer", "перевод на счет")],
                        default="daily",
                        help_text="Выберите способ оплаты",
                        null=True,
                        verbose_name="Способ оплаты",
                    ),
                ),
                (
                    "course_paid",
                    models.ForeignKey(
                        help_text="Укажите оплаченный курс",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments_course",
                        to="materials.course",
                        verbose_name="Оплаченный курс",
                    ),
                ),
                (
                    "lesson_paid",
                    models.ForeignKey(
                        help_text="Укажите оплаченный урок",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments_lesson",
                        to="materials.lesson",
                        verbose_name="Оплаченный урок",
                    ),
                ),
                (
                    "user_payer",
                    models.ForeignKey(
                        help_text="Укажите плательщика",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Плательщик",
                    ),
                ),
            ],
        ),
    ]
