from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateApiView, PaymentsListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="users-update"),

    # payments
    path("payments/", PaymentsListAPIView.as_view(), name="payments-list"),
]
