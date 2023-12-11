from infra.config.connection import DBConnectionHandler
from infra.entities.medico import Medico

class MedicoRepository:

    @staticmethod
    def select_medico_by_id(id_medico):
        with (DBConnectionHandler() as db):
            medico = db.session.query(Medico).filter(Medico.id == id_medico).first()
            return medico

    @staticmethod
    def select_medico_by_crm(numero_crm):
        with (DBConnectionHandler() as db):
            medico = db.session.query(Medico).filter(Medico.numero_crm == numero_crm).first()
            return medico

    @staticmethod
    def select_medico_by_email(email_medico):
        with DBConnectionHandler() as db:
            medico = db.session.query(Medico).filter(Medico.email == email_medico).first()
            return medico

    @staticmethod
    def select_medico_by_name(nome_medico):
        with DBConnectionHandler() as db:
            medico = db.session.query(Medico).filter(Medico.nome == nome_medico).first()
            return medico

    @staticmethod
    def select_all_medicos():
        with DBConnectionHandler() as db:
            data = db.session.query(Medico).all()
            return data

    @staticmethod
    def insert_one_medico(medico):
        with DBConnectionHandler() as db:
            db.session.add(medico)
            db.session.commit()

    @staticmethod
    def update_medico(medico):
        with DBConnectionHandler() as db:
            db.session.query(Medico).filter(Medico.id == medico.id).update({'nome': medico.nome,
                                                                              'especialidade': medico.especialidade,
                                                                              'telefone_contato': medico.telefone_contato,
                                                                              'email': medico.email,
                                                                              'numero_crm': medico.numero_crm,
                                                                              'idade': medico.idade})
            db.session.commit()

    @staticmethod
    def delete_medico(medico):
        with DBConnectionHandler() as db:
            db.session.query(Medico).filter(Medico.nome == medico.nome).update({'ativo': False})
            db.session.commit()