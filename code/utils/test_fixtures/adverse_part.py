from cliente.models import AdversePart, AdversePartAddress


class AdversePartMixin:

    def make_adverse_part(nome, email, numero, cpf_cnpj, tipo):
        adverse_part_data = {
            "nome": nome,
            "email": email,
            "numero": numero,
            "cpf_cnpj": cpf_cnpj,
            "tipo": tipo,
        }

        return AdversePart.objects.create(**adverse_part_data)

    def make_adverse_part_address(parte_adv, endereco, complemento, cep):
        adverse_part_address_data = {
            "endereco": endereco,
            "complemento": complemento,
            "cep": cep,
            "parte_adv": parte_adv
        }

        return AdversePartAddress.objects.create(**adverse_part_address_data)
