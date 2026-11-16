"""Registros demonstrativos para facilitar a apresentação do protótipo.

Os textos são exemplos didáticos e não substituem informações oficiais dos órgãos públicos.
"""

from modelos import Servico


DADOS_EXEMPLO = [
    ("S001", "Agendamento de consulta", "Saúde",
     "Orientações para solicitar atendimento em uma unidade de saúde.",
     "Documento de identificação e cartão do SUS, quando disponível.",
     "Unidade de saúde do município"),
    ("S002", "Retirada de medicamentos", "Saúde",
     "Orientações gerais para retirada de medicamentos na rede pública.",
     "Receita válida e documento de identificação; confirme as regras locais.",
     "Farmácia da rede pública"),
    ("S003", "Atendimento do CRAS", "Assistência social",
     "Orientações para procurar atendimento socioassistencial.",
     "Levar documentos pessoais dos integrantes da família, se disponíveis.",
     "CRAS de referência do cidadão"),
    ("S004", "Cadastro Único", "Assistência social",
     "Informações iniciais sobre inscrição e atualização cadastral.",
     "Documentos dos integrantes da família; confirme a lista exigida.",
     "Posto de atendimento do Cadastro Único"),
    ("S005", "Emissão de documento de identidade", "Documentação e cidadania",
     "Orientações para solicitar ou renovar documento de identidade.",
     "Documentos pessoais exigidos pelo órgão emissor.",
     "Posto oficial de identificação"),
    ("S006", "Solicitação de certidão", "Documentação e cidadania",
     "Informações sobre como solicitar uma certidão em órgão competente.",
     "Dados necessários para localizar o registro; consulte o cartório responsável.",
     "Cartório competente"),
    ("S007", "Matrícula na educação de jovens e adultos", "Educação e qualificação",
     "Orientações para buscar vagas na modalidade de educação de jovens e adultos.",
     "Documento de identificação e histórico escolar, se houver.",
     "Unidade de ensino da rede pública"),
    ("S008", "Cursos de qualificação profissional", "Educação e qualificação",
     "Informações para localizar cursos gratuitos de formação profissional.",
     "Os requisitos variam conforme o curso e a instituição.",
     "Instituição ofertante"),
    ("S009", "Solicitação de coleta de resíduos", "Serviços urbanos",
     "Orientações para solicitar informações ou atendimento sobre coleta urbana.",
     "Endereço e descrição da solicitação.",
     "Central de atendimento municipal"),
    ("S010", "Iluminação pública", "Serviços urbanos",
     "Orientações para comunicar lâmpada apagada ou problema de iluminação.",
     "Endereço ou ponto de referência e descrição do problema.",
     "Canal oficial de serviços urbanos"),
]


def carregar_dados_exemplo(lista):
    """Insere os registros demonstrativos na lista encadeada recebida."""
    for dados in DADOS_EXEMPLO:
        lista.inserir(Servico(*dados))
    return len(DADOS_EXEMPLO)
