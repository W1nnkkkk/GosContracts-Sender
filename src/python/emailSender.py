import smtplib
from config import SENDER_EMAIL, EMAIL_PASSWORD
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template, Environment, FileSystemLoader, select_autoescape


def create_message(top_contracts):
    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('../../table.html')

    message = template.render(items=top_contracts)
    with open("../../my_new_table.html", "w") as fh:
        fh.write(message)

    return message


def send_email_with_contracts(message, email_list):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Топ-10 госконтрактов"
    msg['From'] = SENDER_EMAIL
    msg['To'] = ', '.join(email_list)

    part1 = MIMEText(message, 'html')
    msg.attach(part1)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
        smtp.send_message(msg)