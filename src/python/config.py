import os

from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
email_list = ['tivchenko5442@gmail.com', 'artem.egorov.art@yandex.ru', 'pelaxyt1234@gmail.com']
