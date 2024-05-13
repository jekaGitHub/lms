import smtplib

from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_about_update_materials(email_list):
    """Отправляет сообщение об обновлении материалов."""

    try:
        send_mail('Обновление курса', 'Материалы курса обновлены!', EMAIL_HOST_USER, [email_list], fail_silently=False)
    except smtplib.SMTPException:
        raise smtplib.SMTPException
