from datetime import datetime, time, timedelta
from dateutil.relativedelta import relativedelta
from sqlalchemy import func
import time
from sqlalchemy.orm import joinedload

from infra.config.connection import DBConnectionHandler
from infra.entities.paciente import Paciente
from infra.entities.medico import Medico
from infra.entities.consulta import Consulta


class ConsultaRepository:

    @staticmethod
    def insert_consulta(protocolo, paciente, medico, data_consulta, horario_consulta, tipo_exame, informacoes_adicionais):
        with DBConnectionHandler() as db:
            data_hora_consulta = datetime.strptime(f"{data_consulta} {horario_consulta}", '%d/%m/%Y %H:%M')
            consulta = Consulta()
            #consulta.consulta_protocolo = "AG" + str(int(time.time()))
            consulta.consulta_protocolo = protocolo
            consulta.paciente_id = paciente.id
            consulta.medico_id = medico.id
            consulta.data_consulta = data_hora_consulta
            consulta.tipo_exame = tipo_exame
            consulta.informacoes_adicionais = informacoes_adicionais
            try:
                db.session.add(consulta)
                db.session.commit()
            except Exception as e:
                print(f'Erro ao cadastrar consulta: {e}')

    @staticmethod
    def verificar_consulta_paciente(paciente, data, hora):
        with DBConnectionHandler() as db:
            data_hora_consulta = datetime.strptime(f"{data} {hora}", '%d/%m/%Y %H:%M')
            consulta_existente = db.session.query(Consulta).filter_by(paciente_id=paciente.id,
                                                                      data_consulta=data_hora_consulta).first()

            if consulta_existente:
                return True
            else:
                return False

    @staticmethod
    def verificar_consulta_data_hora(data_consulta, horario_consulta):
        with DBConnectionHandler() as db:
            data_hora_formatada = datetime.strptime(f"{data_consulta} {horario_consulta}", '%d/%m/%Y %H:%M')
            consulta_existente = db.session.query(Consulta).filter_by(data_consulta=data_hora_formatada).first()

            if consulta_existente:
                return True
            else:
                return False

    @staticmethod
    def update_consulta(consulta):
        try:
            with DBConnectionHandler() as db:
                db.session.merge(consulta)
                db.session.commit()
                print("Consulta atualizada com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar consulta: {e}")

    @staticmethod
    def delete_consulta(consulta):
        with DBConnectionHandler as db:
            db.session.delete(consulta)
            db.session.commit()

    @staticmethod
    def select_consultas_protolo(protocolo):
        with DBConnectionHandler() as db:
            consulta = (db.session.query(Consulta)
                        .options(joinedload(Consulta.paciente), joinedload(Consulta.medico))
                        .filter_by(consulta_protocolo=protocolo)
                        .first())
            return consulta

    @staticmethod
    def select_consultas_ativas():
        with DBConnectionHandler() as db:
            consultas = (db.session.query(Consulta.consulta_protocolo, Consulta.data_consulta, Paciente.nome,
                                          Consulta.tipo_exame, Medico.nome)
                         .join(Paciente, Consulta.paciente_id == Paciente.id)
                         .join(Medico, Consulta.medico_id == Medico.id)
                         .filter(Consulta.status.is_(True))
                         .order_by(Consulta.data_consulta.asc()).all())
            return consultas

    @staticmethod
    def select_consultas_ativas_medico(medico_id):
        with DBConnectionHandler() as db:
            consultas = (db.session.query(Consulta.consulta_protocolo, Consulta.data_consulta, Paciente.nome,
                                          Consulta.tipo_exame, Medico.nome)
                         .join(Paciente, Consulta.paciente_id == Paciente.id)
                         .join(Medico, Consulta.medico_id == Medico.id)
                         .filter(Consulta.status.is_(True))
                         .filter(Consulta.medico_id == medico_id)
                         .order_by(Consulta.data_consulta.asc())
                         .all())
            return consultas

    @staticmethod
    def select_consultas_ativas_por_data(data_consulta):
        with DBConnectionHandler() as db:
            try:
                data_consulta_datetime = datetime.strptime(data_consulta, '%d/%m/%Y')
                consultas = (db.session.query(Consulta.consulta_protocolo, Consulta.data_consulta, Paciente.nome,
                                              Consulta.tipo_exame, Medico.nome)
                             .join(Paciente, Consulta.paciente_id == Paciente.id)
                             .join(Medico, Consulta.medico_id == Medico.id)
                             .filter(Consulta.status.is_(True))
                             .filter(
                    func.strftime('%Y-%m-%d', Consulta.data_consulta) == data_consulta_datetime.strftime('%Y-%m-%d'))
                             .order_by(Consulta.data_consulta.asc())
                             .all())

                if not consultas:
                    print('Nenhuma consulta para a semana atual encontrada.')
                    return None
                return consultas

            except Exception as e:
                print(f"Erro: {e}")

    @staticmethod
    def select_consultas_ativas_por_dia():
        with DBConnectionHandler() as db:
            try:
                data_atual = datetime.now().strftime('%d/%m/%Y')
                data_consulta = datetime.strptime(data_atual, '%d/%m/%Y').date()
                consultas = (db.session.query(Consulta.consulta_protocolo, Consulta.data_consulta, Paciente.nome,
                                              Consulta.tipo_exame, Medico.nome)
                             .join(Paciente, Consulta.paciente_id == Paciente.id)
                             .join(Medico, Consulta.medico_id == Medico.id)
                             .filter(Consulta.status.is_(True))
                             .filter(func.strftime('%Y-%m-%d', Consulta.data_consulta) == data_consulta
                             .strftime('%Y-%m-%d'))
                             .order_by(Consulta.data_consulta.asc())
                             .all())
                if not consultas:
                    print('Nenhuma consulta encontrada.')
                    return None
                return consultas

            except Exception as e:
                print(f"Erro 1: {e}")

    @staticmethod
    def select_consultas_para_semana_atual():
        with DBConnectionHandler() as db:
            try:
                data_atual = datetime.now().date()
                inicio_semana = data_atual - timedelta(days=data_atual.weekday())
                fim_semana = inicio_semana + timedelta(days=6)
                consultas_semana = (db.session.query(Consulta.consulta_protocolo, Consulta.data_consulta, Paciente.nome,
                                                     Consulta.tipo_exame, Medico.nome)
                                    .join(Paciente, Consulta.paciente_id == Paciente.id)
                                    .join(Medico, Consulta.medico_id == Medico.id)
                                    .filter(Consulta.status.is_(True))
                                    .filter(
                    func.strftime('%Y-%m-%d', Consulta.data_consulta).between(inicio_semana, fim_semana))
                                    .order_by(Consulta.data_consulta.asc())
                                    .all())

                if not consultas_semana:
                    print('Nenhuma consulta para a semana atual encontrada.')
                    return None

                return consultas_semana

            except Exception as e:
                print(f"Erro: {e}")

    @staticmethod
    def select_consultas_para_semana_atual_medico(medico_id):
        with DBConnectionHandler() as db:
            try:
                data_atual = datetime.now().date()
                inicio_semana = data_atual - timedelta(days=data_atual.weekday())
                fim_semana = inicio_semana + timedelta(days=6)
                consultas_semana = (db.session.query(Consulta.consulta_protocolo, Consulta.data_consulta, Paciente.nome,
                                                     Consulta.tipo_exame, Medico.nome)
                                    .join(Paciente, Consulta.paciente_id == Paciente.id)
                                    .join(Medico, Consulta.medico_id == Medico.id)
                                    .filter(Consulta.status.is_(True))
                                    .filter(Consulta.medico_id == medico_id)
                                    .filter(
                    func.strftime('%Y-%m-%d', Consulta.data_consulta).between(inicio_semana, fim_semana))
                                    .order_by(Consulta.data_consulta.asc())
                                    .all())

                if not consultas_semana:
                    print('Nenhuma consulta para a semana atual encontrada.')
                    return None
                return consultas_semana

            except Exception as e:
                print(f"Erro: {e}")

    @staticmethod
    def select_consultas_para_mes_atual():
        with DBConnectionHandler() as db:
            try:
                data_atual = datetime.now().date()
                inicio_mes = data_atual.replace(day=1)
                proximo_mes = inicio_mes.replace(month=inicio_mes.month % 12 + 1,
                                                 year=inicio_mes.year + inicio_mes.month // 12)
                fim_mes = proximo_mes - timedelta(days=1)
                consultas_mes = (db.session.query(Consulta.consulta_protocolo, Consulta.data_consulta, Paciente.nome,
                                                  Consulta.tipo_exame, Medico.nome)
                                 .join(Paciente, Consulta.paciente_id == Paciente.id)
                                 .join(Medico, Consulta.medico_id == Medico.id)
                                 .filter(Consulta.status.is_(True))
                                 .filter(func.strftime('%Y-%m-%d', Consulta.data_consulta).between(inicio_mes, fim_mes))
                                 .order_by(Consulta.data_consulta.asc())
                                 .all())

                if not consultas_mes:
                    print('Nenhuma consulta para o mês atual encontrada.')
                    return None

                return consultas_mes

            except Exception as e:
                print(f"Erro: {e}")

    @staticmethod
    def select_consultas_para_mes_atual_medico(medico_id):
        with DBConnectionHandler() as db:
            try:
                data_atual = datetime.now().date()
                inicio_mes = data_atual.replace(day=1)
                proximo_mes = inicio_mes.replace(month=inicio_mes.month % 12 + 1,
                                                 year=inicio_mes.year + inicio_mes.month // 12)
                fim_mes = proximo_mes - timedelta(days=1)
                consultas_mes = (db.session.query(Consulta.consulta_protocolo, Consulta.data_consulta, Paciente.nome,
                                                  Consulta.tipo_exame, Medico.nome)
                                 .join(Paciente, Consulta.paciente_id == Paciente.id)
                                 .join(Medico, Consulta.medico_id == Medico.id)
                                 .filter(Consulta.status.is_(True))
                                 .filter(Consulta.medico_id == medico_id)
                                 .filter(func.strftime('%Y-%m-%d', Consulta.data_consulta).between(inicio_mes, fim_mes))
                                 .order_by(Consulta.data_consulta.asc())
                                 .all())

                if not consultas_mes:
                    print('Nenhuma consulta para o mês atual encontrada.')
                    return None

                return consultas_mes

            except Exception as e:
                print(f"Erro: {e}")

    @staticmethod
    def select_consultas_ativas_por_medico_e_data(medico_id, data_consulta):
        with DBConnectionHandler() as db:
            try:
                if data_consulta == '//':
                    data_consulta = datetime.now().date()
                else:
                    data_consulta = datetime.strptime(data_consulta, '%d/%m/%Y').date()
                    consultas = (db.session.query(Consulta.consulta_protocolo, Consulta.data_consulta, Paciente.nome,
                                                  Consulta.tipo_exame, Medico.nome)
                                 .join(Paciente, Consulta.paciente_id == Paciente.id)
                                 .join(Medico, Consulta.medico_id == Medico.id)
                                 .filter(Consulta.status.is_(True))
                                 .filter(Consulta.medico_id == medico_id)
                                 .filter(func.strftime('%Y-%m-%d', Consulta.data_consulta) == data_consulta.strftime('%Y-%m-%d'))
                                 .order_by(Consulta.data_consulta.asc())
                                 .all())
                if not consultas:
                    print('Nenhuma consulta encontrada.')
                    return None
                return consultas

            except Exception as e:
                print(f"Erro 1: {e}")

    @staticmethod
    def select_consultas_para_mes_atual_teste():
        with DBConnectionHandler() as db:
            try:
                data_atual = datetime.now().date()
                inicio_mes = data_atual.replace(day=1)
                proximo_mes = inicio_mes + relativedelta(months=1)
                fim_mes = proximo_mes - timedelta(days=1)
                consultas_mes = (db.session.query(Consulta.consulta_protocolo, Consulta.data_consulta, Paciente.nome,
                                                  Consulta.tipo_exame, Medico.nome)
                                 .join(Paciente, Consulta.paciente_id == Paciente.id)
                                 .join(Medico, Consulta.medico_id == Medico.id)
                                 .filter(Consulta.status.is_(True))
                                 .filter(func.strftime('%Y-%m-%d', Consulta.data_consulta).between(inicio_mes, fim_mes))
                                 .order_by(Consulta.data_consulta.asc())
                                 .all())

                if not consultas_mes:
                    print('Nenhuma consulta para o mês atual encontrada.')
                    return None

                return consultas_mes

            except Exception as e:
                print(f"Erro: {e}")
