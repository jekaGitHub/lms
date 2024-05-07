from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson
from materials.validators import UrlValidator


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [UrlValidator(field='url')]


class CourseSerializer(ModelSerializer):
    lessons_count = serializers.SerializerMethodField()

    lessons_info = LessonSerializer(
        source='lessons',
        many=True,
        read_only=True,
    )

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_count(self, instance):
        return instance.lessons.count()
