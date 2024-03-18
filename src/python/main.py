from emailSender import create_message, send_email_with_contracts
from contracts import get_top_contracts, get_contracts, get_week
from config import email_list


def main():
    result = get_contracts(daterange=get_week(), sort='-price')
    message = create_message(get_top_contracts(result))

    send_email_with_contracts(message, email_list)


main()
