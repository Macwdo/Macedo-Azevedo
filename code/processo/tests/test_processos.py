from django.urls import reverse
from rest_framework.test import APITestCase
from pytest import mark


class ProcessoTest(APITestCase):

    def test_processo_create(self):
        request = self.client.get(
            reverse("processos:processo-get", kwargs={"pk": 1})
        )
        self.assertEqual(request.status_code, 401)
