from .models import MAUser


class EmailAuthBackend:
    def authenticate(self, request, email=None, password=None):
        try:
            user = MAUser.objects.get(email=email)

            if user.check_password(password):
                return user
            return None
        except MAUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MAUser.objects.get(pk=user_id)
        except MAUser.DoesNotExist:
            return None
