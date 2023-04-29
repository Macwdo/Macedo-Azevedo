from django.contrib.auth.models import User
from django.urls import reverse


class UtilsMixin:
    def get_jwt(self, username, password, client) -> dict:
        data = {
            "username": username,
            "password": password
        }
        response = client.post(reverse("token"), data=data)
        return response.data.get("access", None)

    def make_user(self, username: str, password: str, email: str) -> User:
        user = User.objects.create(
            username=username, password=password, email=email
        )
        user.set_password(password)
        user.save()
        return user
