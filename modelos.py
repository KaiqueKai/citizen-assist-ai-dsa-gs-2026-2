"""Modelos de dados do Citizen Assist AI."""


class Servico:
    """Representa um serviço ou uma orientação disponibilizada ao cidadão."""

    CAMPOS_OBRIGATORIOS = ("titulo", "categoria", "descricao")

    def __init__(self, identificador, titulo, categoria, descricao,
                 requisitos="Não informado", local_atendimento="Não informado"):
        self.identificador = self._limpar(identificador)
        self.titulo = self._limpar(titulo)
        self.categoria = self._limpar(categoria)
        self.descricao = self._limpar(descricao)
        self.requisitos = self._limpar(requisitos) or "Não informado"
        self.local_atendimento = self._limpar(local_atendimento) or "Não informado"

        if not self.identificador:
            raise ValueError("O identificador não pode ficar vazio.")
        self._validar_campos_obrigatorios()

    @staticmethod
    def _limpar(valor):
        if valor is None:
            return ""
        return str(valor).strip()

    def _validar_campos_obrigatorios(self):
        for campo in self.CAMPOS_OBRIGATORIOS:
            if not getattr(self, campo):
                raise ValueError(f"O campo {campo} não pode ficar vazio.")

    def atualizar(self, **campos):
        """Atualiza campos permitidos sem alterar o identificador único."""
        campos_permitidos = {
            "titulo", "categoria", "descricao", "requisitos", "local_atendimento"
        }
        desconhecidos = set(campos) - campos_permitidos
        if desconhecidos:
            raise ValueError("Campo(s) não permitido(s): " + ", ".join(sorted(desconhecidos)))

        novos_valores = {chave: self._limpar(valor) for chave, valor in campos.items()}
        for campo in self.CAMPOS_OBRIGATORIOS:
            if campo in novos_valores and not novos_valores[campo]:
                raise ValueError(f"O campo {campo} não pode ficar vazio.")

        for campo, valor in novos_valores.items():
            if campo in ("requisitos", "local_atendimento") and not valor:
                valor = "Não informado"
            setattr(self, campo, valor)

    def __str__(self):
        return (
            f"ID: {self.identificador}\n"
            f"Título: {self.titulo}\n"
            f"Categoria: {self.categoria}\n"
            f"Descrição: {self.descricao}\n"
            f"Requisitos: {self.requisitos}\n"
            f"Local de atendimento: {self.local_atendimento}"
        )
