from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class ProcessoTest(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='macwdo', password='123', email='default@email.co'
        )
        return super().setUp()

    def test_list_advogados(self):
        self.assertEqual(1, 1)
