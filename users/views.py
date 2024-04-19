from rest_framework.generics import UpdateAPIView

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserUpdateApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
