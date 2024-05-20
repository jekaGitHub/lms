# Generated by Django 4.2.2 on 2024-05-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_alter_payments_payment_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True,
                help_text="Укажите город",
                max_length=35,
                null=True,
                verbose_name="Город",
            ),
        ),
    ]
