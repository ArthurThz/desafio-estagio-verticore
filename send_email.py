import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

file_path = "C:/Users/lauto/OneDrive/Área de Trabalho/Projetos/desafio-verticore-estagio/bot-desafio-verticore/dados_ibge.xlsx"
attachment = open(file_path,'rb')

att = MIMEBase('application','octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

att.add_header('Content-Disposition',f'attachment; filename=dados_ibge.xls')
attachment.close()



host = "smtp-mail.outlook.com"
port = "587"
login = "desafio-estagio@outlook.com"
senha = "SenhaDoDesafio"


server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()

server.login(login,senha)

corpo = "Olá, segue anexo a planilha com os dados colhidos do site do IBGE"
email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = login
email_msg['Subject'] = "Dados colhidos com Python"

email_msg.attach(MIMEText(corpo,'plain'))
email_msg.attach(att)

def sendEmail():
    server.sendmail(email_msg['From'],email_msg['To'], email_msg.as_string())
    server.quit()