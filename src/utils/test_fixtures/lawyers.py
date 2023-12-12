from typing import Union

from django.contrib.auth.models import User

from advogado.models import Advogado


class LawyerMixin:
    def make_lawyer(
        self, nome: str, email: str, oab: str, usuario=Union[User, None]
    ) -> Advogado:
        lawyer_data = {
            'nome': nome,
            'email': email,
            'oab': oab,
        }
        if usuario:
            lawyer_data['usuario'] = usuario

        return Advogado.objects.create(**lawyer_data)
