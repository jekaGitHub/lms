from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateApiView

app_name = UsersConfig.name

urlpatterns = [
    path("users/<int:pk>/update/", UserUpdateApiView.as_view(), name="users_update"),
]
