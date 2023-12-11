from __future__ import annotations

from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.config.base import Base

class Paciente(Base):
    __tablename__ = 'pacientes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    cpf: Mapped[str] = mapped_column(nullable=False, unique=True)
    idade: Mapped[int] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    telefone_contato: Mapped[str] = mapped_column(nullable=False)
    nome_emergencia: Mapped[str] = mapped_column(nullable=False)
    telefone_emergencia: Mapped[str] = mapped_column(nullable=False)
    numero_seguro: Mapped[str] = mapped_column(nullable=True, unique=True)
    historico_medico: Mapped[str] = mapped_column(nullable=True)
    ativo: Mapped[bool] = mapped_column(default=True, nullable=False)
    consultas = relationship("Consulta", back_populates="paciente", cascade="save-update")


    def campos_obrigatorios_preenchidos(self):
        campos_obrigatorios = [
            self.nome,
            self.cpf,
            self.idade,
            self.email,
            self.telefone_contato,
            self.nome_emergencia,
            self.telefone_emergencia
        ]

        for campo in campos_obrigatorios:
            if not campo:
                return False

        return True

    def __repr__(self):
        return f'Paciente [nome= {self.nome}, cpf={self.cpf}, idade={self.idade}, email={self.email}, telefone_contato={self.telefone_contato}, nome_emergencia={self.nome_emergencia}, telefone_emergencia={self.telefone_emergencia}, numero_seguro={self.numero_seguro}, historico_medico={self.historico_medico}'