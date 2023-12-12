from registry.models import ClienteEndereco, Re


class ClientsMixin:

    def make_client(nome, email, numero, cpf_cnpj, tipo):
        client_data = {
            "nome": nome,
            "email": email,
            "numero": numero,
            "cpf_cnpj": cpf_cnpj,
            "tipo": tipo,
        }

        return Cliente.objects.create(**client_data)

    def make_client_address(cliente, endereco, complemento, cep):
        client_address_data = {
            "endereco": endereco,
            "complemento": complemento,
            "cep": cep,
            "cliente": cliente
        }

        return ClienteEndereco.objects.create(**client_address_data)
