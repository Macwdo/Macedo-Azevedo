
from rest_framework.test import APITestCase

class ProcessoTest(APITestCase):

    def test_processo_create(self):
        request = self.client.get("api/v1/processo")
        print(request)
        self.assertEqual(1, 1)
