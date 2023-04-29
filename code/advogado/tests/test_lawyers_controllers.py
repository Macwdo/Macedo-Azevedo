from rest_framework.test import APITestCase
from django.urls import reverse
from utils.test_fixtures.lawyers import LawyerMixin
from utils.test_fixtures.utils_test import UtilsMixin


class LawyersTestCase(APITestCase, LawyerMixin, UtilsMixin):

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

    def test_list_lawyers(self):
        response = self.client.get(
            reverse("advogado-list"), HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(200, response.status_code)

    def test_create_lawyers(self):
        data = {
            "nome": "Sandra Cristina",
            "email": "default@email.co",
            "oab": "RJ127324",
            "usuario": self.make_user(username="user", password="123", email="default@email.co").pk
        }
        url = reverse("advogado-list")
        response = self.client.post(
            url, data=data, HTTP_AUTHORIZATION=f"Bearer {self.token}", format="json"
        )
        self.assertEqual(201, response.status_code)

    def test_retrieve_lawyers(self):
        url = reverse("advogado-detail", kwargs={"pk": self.lawyer.pk})
        response = self.client.get(
            url, HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(200, response.status_code)

    def test_update_lawyers(self):
        data = {
            "nome": "Danilo Macedo",
            "email": "default@email.co",
            "oab": "RJ127324",
            "usuario": self.user.pk
        }
        url = reverse("advogado-detail", kwargs={"pk": self.lawyer.pk})
        response = self.client.put(
            url, data=data, HTTP_AUTHORIZATION=f"Bearer {self.token}", format="json"
        )
        self.assertEqual(data["nome"], response.data["nome"])

    def test_partial_update_lawyers(self):
        data = {
            "nome": "Danilo"
        }
        url = reverse("advogado-detail", kwargs={"pk": self.lawyer.pk})
        response = self.client.patch(
            url, data=data, HTTP_AUTHORIZATION=f"Bearer {self.token}", format="json"
        )
        self.assertEqual(response.data["nome"], data["nome"])

    def test_destroy_lawyers(self):
        url = reverse("advogado-detail", kwargs={"pk": self.lawyer.pk})
        response = self.client.delete(
            url, HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )
        self.assertEqual(204, response.status_code)
