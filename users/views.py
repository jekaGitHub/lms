from rest_framework.generics import UpdateAPIView, ListAPIView

from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer


# Create your views here.
class UserUpdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentsListAPIView(ListAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
