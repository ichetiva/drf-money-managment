from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users import views

urlpatterns = [
    # auth
    path("auth/token/", obtain_auth_token, name="obtain-auth-token"),

    # users
    path("users/create/", views.CreateUserAPIView.as_view(), name="create-user"),
    path("users/me/", views.GetUserAPIView.as_view(), name="get-me"),
]
