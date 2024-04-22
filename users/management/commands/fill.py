import json

from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import User, Payments


class Command(BaseCommand):

    @staticmethod
    def json_read_users():
        # Здесь мы получаем данные из фикстуры с пользователями
        users = []

        with open("users_data.json", 'r') as f:
            data = json.load(f)

        for item in data:
            if item['model'] == 'users.user':
                users.append(item)

        return users

    @staticmethod
    def json_read_courses():
        # Здесь мы получаем данные из фикстуры с курсами
        courses = []

        with open("materials_data.json", 'r') as f:
            data = json.load(f)

        for item in data:
            if item['model'] == 'materials.course':
                courses.append(item)

        return courses

    @staticmethod
    def json_read_lessons():
        # Здесь мы получаем данные из фикстуры с уроками
        lessons = []

        with open("materials_data.json", 'r') as f:
            data = json.load(f)

        for item in data:
            if item['model'] == 'materials.lesson':
                lessons.append(item)

        return lessons

    @staticmethod
    def json_read_payments():
        # Здесь мы получаем данные из фикстуры с платежами
        payments = []

        with open("users_data.json", 'r') as f:
            data = json.load(f)

        for item in data:
            if item['model'] == 'users.payments':
                payments.append(item)

        return payments

    def handle(self, *args, **options):

        # Удалите всех пользователей
        User.objects.all().delete()
        # Удалите все курсы
        Course.objects.all().delete()
        # Удалите все уроки
        Lesson.objects.all().delete()
        # Удалите все платежи
        Payments.objects.all().delete()

        # Списки для хранения объектов
        user_for_create = []
        course_for_create = []
        lesson_for_create = []
        payments_for_create = []

        # Обходим все значения пользователей из фикстуры для получения информации об одном объекте
        for user in Command.json_read_users():
            user_for_create.append(
                User(id=user['pk'],
                     password=user['fields']['password'],
                     email=user['fields']['email'],
                     phone=user['fields']['phone'],
                     city=user['fields']['city'],
                     avatar=user['fields']['avatar'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        User.objects.bulk_create(user_for_create)

        # Обходим все значения курсов из фикстуры для получения информации об одном объекте
        for course in Command.json_read_courses():
            course_for_create.append(
                Course(id=course['pk'],
                       name=course['fields']['name'],
                       image=course['fields']['image'],
                       description=course['fields']['description'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Course.objects.bulk_create(course_for_create)

        # Обходим все значения уроков из фикстуры для получения информации об одном объекте
        for lesson in Command.json_read_lessons():
            lesson_for_create.append(
                Lesson(id=lesson['pk'],
                       name=lesson['fields']['name'],
                       course=Course.objects.get(pk=lesson['fields']['course']),
                       description=lesson['fields']['description'],
                       image=lesson['fields']['image'],
                       url=lesson['fields']['url'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Lesson.objects.bulk_create(lesson_for_create)

        # Обходим все значения платежей из фикстуры для получения информации об одном объекте
        for payment in Command.json_read_payments():
            lesson_paid = Lesson.objects.filter(pk=payment['fields']['lesson_paid']).first()
            course_paid = Course.objects.filter(pk=payment['fields']['course_paid']).first()
            payments_for_create.append(
                Payments(id=payment['pk'],
                         user_payer=User.objects.get(pk=payment['fields']['user_payer']),
                         payment_date=payment['fields']['payment_date'],
                         course_paid=course_paid,
                         lesson_paid=lesson_paid,
                         payment_amount=payment['fields']['payment_amount'],
                         payment_method=payment['fields']['payment_method'])
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Payments.objects.bulk_create(payments_for_create)
