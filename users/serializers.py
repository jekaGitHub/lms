from rest_framework.serializers import ModelSerializer

from users.models import User, Payments


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(ModelSerializer):
    history_payments = PaymentsSerializer(
        source="payments",
        many=True,
    )

    class Meta:
        model = User
        fields = "__all__"


class UserForCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
