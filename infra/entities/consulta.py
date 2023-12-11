from __future__ import annotations

from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.config.base import Base

class Consulta(Base):
    __tablename__ = 'consultas'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    consulta_protocolo: Mapped[str] = mapped_column(unique=True, nullable=False)
    paciente_id: Mapped[int] = mapped_column(ForeignKey("pacientes.id"))
    medico_id: Mapped[int] = mapped_column(ForeignKey("medicos.id"))
    data_consulta: Mapped[datetime] = mapped_column(nullable=False)
    tipo_exame: Mapped[str] = mapped_column(nullable=False)
    informacoes_adicionais: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[bool] = mapped_column(default=True, nullable=False)
    motivo: Mapped[str] = mapped_column(nullable=True)
    paciente = relationship("Paciente", back_populates="consultas")
    medico = relationship("Medico", back_populates="consultas")