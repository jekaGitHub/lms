from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import UserCreateApiView, UserUpdateApiView, PaymentsListAPIView, UserRetrieveApiView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="users-update"),
    path("<int:pk>/", UserRetrieveApiView.as_view(), name="users-retrieve"),

    # payments
    path("payments/", PaymentsListAPIView.as_view(), name="payments-list"),
]
