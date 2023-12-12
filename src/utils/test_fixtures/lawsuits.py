from processo.models import Processos, ProcessosAnexos, ProcessosHonorarios


class LawsuitsMixin:
    def make_lawsuit(
        cliente,
        cliente_de,
        codigo_processo,
        advogado_responsavel,
        parte_adversa,
        posicao,
        assunto,
        municipio,
        estado,
        n_vara,
        vara,
        colaborador=None,
    ):
        lawsuit_data = {
            'cliente': cliente,
            'cliente_de': cliente_de,
            'codigo_processo': codigo_processo,
            'advogado_responsavel': advogado_responsavel,
            'parte_adversa': parte_adversa,
            'posicao': posicao,
            'assunto': assunto,
            'municipio': municipio,
            'estado': estado,
            'n_vara': n_vara,
            'vara': vara,
        }

        if colaborador:
            lawsuit_data['colaborador'] = colaborador
        return Processos.objects.create(**lawsuit_data)

    def make_lawsuit_values(
        referente, processo, advogado_responsavel, valor, ganho
    ):
        lawsuit_values_data = {
            'referente': referente,
            'processo': processo,
            'advogado_responsavel': advogado_responsavel,
            'valor': valor,
            'ganho': ganho,
        }
        return ProcessosHonorarios.objects.create(**lawsuit_values_data)

    def make_lawsuit_files(nome_do_anexo, processo):
        lawsuit_files_data = {
            'nome_do_anexo': nome_do_anexo,
            'processo': processo,
            'arquivo': './examplefile.txt',
        }

        return ProcessosAnexos.objects.create(**lawsuit_files_data)
