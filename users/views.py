from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer, UserForCreateSerializer


# Create your views here.
class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserForCreateSerializer

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserUpdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentsListAPIView(ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('course_paid', 'lesson_paid', 'payment_method')
    ordering_fields = ('payment_date',)
