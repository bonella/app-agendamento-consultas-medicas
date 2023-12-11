from __future__ import annotations

from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.config.base import Base

class Medico(Base):
    __tablename__ = 'medicos'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    especialidade: Mapped[str] = mapped_column(nullable=False)
    telefone_contato: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    numero_crm: Mapped[str] = mapped_column(nullable=False, unique=True)
    idade: Mapped[int] = mapped_column(nullable=False)
    ativo: Mapped[bool] = mapped_column(default=True, nullable=False)
    consultas = relationship("Consulta", back_populates="medico", cascade="save-update")


    def __repr__(self):
        return f'Medico[nome = {self.nome}, especialidade={self.especialidade}, telefone_contato={self.telefone_contato}, email={self.email}, numero_crm={self.numero_crm}], idade={self.idade}'

    def campos_obrigatorios_preenchidos(self):
        campos_obrigatorios = [
            self.nome,
            self.especialidade,
            self.telefone_contato,
            self.email,
            self.numero_crm
        ]

        for campo in campos_obrigatorios:
            if not campo:
                return False

        return True
