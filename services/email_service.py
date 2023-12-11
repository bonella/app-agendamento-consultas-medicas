import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ServicoEmail:
    def __init__(self, configuracao):
        self.configuracao = configuracao

    def enviar_email_paciente(self, nome_paciente, destinatario, medico, protocolo, data, hora):
        mensagem = MIMEMultipart('alternative')
        mensagem['From'] = self.configuracao.remetente
        mensagem['To'] = destinatario
        mensagem['Subject'] = f'Lembrete de consulta médica - Protocolo: {protocolo}'

        numero_telefone = '5548999999999'  # Seu numero de telefone WhatsApp
        link_whatsapp = f"""<h3><a href="https://api.whatsapp.com/send?phone={numero_telefone}&text=">WhatsApp</a></h3>"""

        corpo_mensagem = (f'Esta mensagem é apenas para lembrar você sobre a consulta nº: {protocolo}, \n'
                           f'que está marcada para a data {data} às {hora}, com o médico {medico}. '
                           f'Caso desejar remarcar essa consulta, favor entrar em contato pelo telefone (48) 99999-9999, ou nos envie um mensagem via: {link_whatsapp}')

        texto = "Olá,\n\n" + corpo_mensagem
        parte_texto = MIMEText(texto, 'plain')

        html = f"""
         <html>
           <head>
             <style>
               body {{
                 font-family: Arial, sans-serif;
                 background-color: #f4f4f4;
                 padding: 20px;
                 margin: 0;
               }}
               .container {{
                 max-width: 600px;
                 margin: 0 auto;
                 background-color: #fff;
                 padding: 20px;
                 border-radius: 8px;
                 box-shadow: 0 0 13px rgba(0, 0, 0, 0.1);
               }}
               h1 {{
                 color: #333;
               }}
               p {{
                 color: #666;
                 line-height: 1.6;
               }}
             </style>
           </head>
           <body>
             <div class="container">
               <h1>Olá!</h1>
               <h2>{nome_paciente}, </h2> <p>{corpo_mensagem}</p> 
               <p>Atenciosamente, 
               <p>Equipe 5
             </div>
           </body>
         </html>
         """
        parte_html = MIMEText(html, 'html')

        mensagem.attach(parte_texto)
        mensagem.attach(parte_html)

        try:
            server = smtplib.SMTP(self.configuracao.servidor_smtp, self.configuracao.porta_smtp)
            server.starttls()
            server.login(self.configuracao.remetente, self.configuracao.senha)
            server.sendmail(self.configuracao.remetente, destinatario, mensagem.as_string())
            server.quit()
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar o e-mail: {str(e)}")

    def enviar_email_paciente_reagendamento(self, nome_paciente, destinatario, medico, protocolo, data, hora):
        mensagem = MIMEMultipart('alternative')
        mensagem['From'] = self.configuracao.remetente
        mensagem['To'] = destinatario
        mensagem['Subject'] = f'Lembrete de consulta médica - Protocolo: {protocolo}'

        numero_telefone = '5548998666656'
        link_whatsapp = f"""<h3><a href="https://api.whatsapp.com/send?phone={numero_telefone}&text=">WhatsApp</a></h3>"""

        corpo_mensagem = (f'Esta mensagem é apenas para lembrar você sobre a consulta nº: {protocolo}, \n'
                           f'que foi remarcada para a data {data} às {hora}, com o médico {medico}. '
                           f'Caso desejar remarcar essa consulta, favor entrar em contato pelo telefone (48) 99999-8898, ou nos envie um mensagem via: {link_whatsapp}')

        texto = "Olá,\n\n" + corpo_mensagem
        parte_texto = MIMEText(texto, 'plain')

        html = f"""
         <html>
           <head>
             <style>
               body {{
                 font-family: Arial, sans-serif;
                 background-color: #f4f4f4;
                 padding: 20px;
                 margin: 0;
               }}
               .container {{
                 max-width: 600px;
                 margin: 0 auto;
                 background-color: #fff;
                 padding: 20px;
                 border-radius: 8px;
                 box-shadow: 0 0 13px rgba(0, 0, 0, 0.1);
               }}
               h1 {{
                 color: #333;
               }}
               p {{
                 color: #666;
                 line-height: 1.6;
               }}
             </style>
           </head>
           <body>
             <div class="container">
               <h1>Olá!</h1>
               <h2>{nome_paciente}, </h2> <p>{corpo_mensagem}</p> 
               <p>Atenciosamente, 
               <p>Equipe 5
             </div>
           </body>
         </html>
         """
        parte_html = MIMEText(html, 'html')

        mensagem.attach(parte_texto)
        mensagem.attach(parte_html)

        try:
            server = smtplib.SMTP(self.configuracao.servidor_smtp, self.configuracao.porta_smtp)
            server.starttls()
            server.login(self.configuracao.remetente, self.configuracao.senha)
            server.sendmail(self.configuracao.remetente, destinatario, mensagem.as_string())
            server.quit()
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar o e-mail: {str(e)}")