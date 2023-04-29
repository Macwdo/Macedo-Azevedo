from rest_framework.test import APITestCase
from django.urls import reverse
from utils.test_fixtures.lawyers import LawyerMixin
from utils.test_fixtures.utils_test import UtilsMixin


class AdvogadoTest(APITestCase, LawyerMixin, UtilsMixin):

    def setUp(self) -> None:
        self.user_data = {
            "username": "macwdo",
            "password": "123",
            "email": "default@email.co"
        }

        self.user = self.make_user(
            self.user_data["username"],
            self.user_data["password"],
            self.user_data["email"]
        )

        self.lawyer = self.make_lawyer(
            nome="Sandra Cristina",
            email="default@email.co",
            oab="RJ120324",
            usuario=self.user
        )

        self.token = self.get_jwt(
            username=self.user_data["username"],
            password=self.user_data["password"],
            client=self.client
        )

    def test_list_advogados(self):
        response = self.client.get(
            reverse("advogado-list"), HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.assertEqual(200, response.status_code)

    def test_get_lawyers_list(self):
        response = self.client.get(
            reverse("advogado-detail", kwargs={"pk": self.lawyer.pk}), HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(200, response.status_code)

    def test_get_lawyers_detail(self):
        response = self.client.get(
            reverse("advogado-detail", kwargs={"pk": self.lawyer.pk}), HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(200, response.status_code)

    def test_partial_update_lawyers_detail(self):
        data = {
            "nome": "Danilo"
        }
        response = self.client.patch(
            reverse("advogado-detail", kwargs={"pk": self.lawyer.pk}), data=data, HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

        self.assertEqual(200, response.status_code)

    def test_delete_lawyers(self):
        response = self.client.delete(
            reverse("advogado-detail", kwargs={"pk": self.lawyer.pk}), HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(204, response.status_code)
