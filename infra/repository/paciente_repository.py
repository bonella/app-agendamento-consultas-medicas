from infra.config.connection import DBConnectionHandler
from infra.entities.paciente import Paciente

class PacienteRepository:

    @staticmethod
    def insert_one_paciente(paciente):
        with DBConnectionHandler() as db:
            db.session.add(paciente)
            db.session.commit()

    @staticmethod
    def select_paciente_by_id(id_paciente):
        with (DBConnectionHandler() as db):
            paciente = db.session.query(Paciente).filter(Paciente.id == id_paciente).first()
            return paciente

    @staticmethod
    def select_paciente_by_cpf(cpf_paciente):
        with DBConnectionHandler() as db:
            paciente = db.session.query(Paciente).filter(Paciente.cpf == cpf_paciente).first()
            return paciente

    @staticmethod
    def select_paciente_by_email(email_paciente):
        with DBConnectionHandler() as db:
            paciente = db.session.query(Paciente).filter(Paciente.email == email_paciente).first()
            return paciente

    @staticmethod
    def select_paciente_by_numero_seguro(numero_seguro):
        with DBConnectionHandler() as db:
            paciente = db.session.query(Paciente).filter(Paciente.numero_seguro == numero_seguro).first()
            return paciente

    @staticmethod
    def update_paciente(paciente):
        with DBConnectionHandler() as db:
            db.session.query(Paciente).filter(Paciente.id == paciente.id).update({'nome': paciente.nome,
                                                                                  'cpf': paciente.cpf,
                                                                                  'idade': paciente.idade,
                                                                                  'email': paciente.email,
                                                                                  'telefone_contato': paciente.telefone_contato,
                                                                                  'nome_emergencia': paciente.nome_emergencia,
                                                                                  'telefone_emergencia': paciente.telefone_emergencia,
                                                                                  'numero_seguro': paciente.numero_seguro,
                                                                                  'historico_medico': paciente.historico_medico})
            db.session.commit()

    @staticmethod
    def delete_paciente(data):
        with DBConnectionHandler() as db:
            db.session.query(Paciente).filter(Paciente.id == data.id).update({'ativo': False})
            db.session.commit()