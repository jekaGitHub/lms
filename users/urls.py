from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateApiView, PaymentsListAPIView, UserRetrieveApiView

app_name = UsersConfig.name

urlpatterns = [
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="users-update"),
    path("<int:pk>/", UserRetrieveApiView.as_view(), name="users-retrieve"),

    # payments
    path("payments/", PaymentsListAPIView.as_view(), name="payments-list"),
]
