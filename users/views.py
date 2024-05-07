from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from materials.models import Course
from users.models import User, Payments, Subscription
from users.permissions import IsOwner
from users.serializers import UserSerializer, PaymentsSerializer, UserForCreateSerializer, UserUpdateSerializer, \
    SubscriptionSerializer


# Create your views here.
class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserForCreateSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserUpdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class UserRetrieveApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.id == self.request.user.id:
            serializer = self.get_serializer(instance)
        else:
            serializer = UserUpdateSerializer
        return Response(serializer.data)


class PaymentsListAPIView(ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ('course_paid', 'lesson_paid', 'payment_method')
    ordering_fields = ('payment_date',)


class SubscriptionCreateApiView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'Подписка удалена'
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'Подписка добавлена'
        return Response({"message": message})
