import requests
import logging
from dickt_key_finder import recurse_find_key
from datetime import timedelta, date, datetime

logging.basicConfig(filename='../../logs/logfile.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(funcName)s || %(message)s')


def get_contracts(**kwargs):
    url = f"http://openapi.clearspending.ru/restapi/v3/contracts/search/"

    params = {**kwargs}
    logging.info("Началось выполнение функции get_contacts" + url, params)
    try:
        req = requests.get(url, params)
        logging.info(req)
    except Exception as e:
        logging.error('Ошибка перехода по ссылке')
        logging.exception(e)

    try:
        data = req.json()
        logging.info("Операция преобразования в json успешна")
        return data
    except Exception as e:
        logging.error('Ошибка преобразования в JSON')
        logging.exception(e)


def get_week(day=None):
    if day == None:
        start_date = date.today()
    else:
        start_date = datetime.datetime.strptime(day, "%d.%m.%Y")

    end_date = start_date - timedelta(weeks=1)
    date_range = f"{end_date.strftime('%d.%m.%Y')}-{start_date.strftime('%d.%m.%Y')}"

    return date_range


def get_top_contracts(json_data):
    data = json_data['contracts']['data']
    top_contracts = []

    for contract in data:
        contract_dict = {}
        try:
            urls = [recurse_find_key('url', item) for item in contract['scan']]
            signDate = recurse_find_key('signDate', contract)
            numReg = recurse_find_key('regNum', contract)
            price = recurse_find_key('price', contract)
            regionCode = recurse_find_key('regionCode', contract)
            customer_fullanme = recurse_find_key('customer', contract)['fullName']
            customer_inn = recurse_find_key('customer', contract)['inn']
            products = [(recurse_find_key('name', item)) for item in contract['products']]

            contract_dict['url'] = urls
            contract_dict['sign_date'] = signDate
            contract_dict['num_reg'] = numReg
            contract_dict['price'] = price
            contract_dict['region_code'] = regionCode
            contract_dict['customer_fullname'] = customer_fullanme
            contract_dict['customer_inn'] = customer_inn
            contract_dict['products'] = products

            top_contracts.append(contract_dict)
        except Exception as e:
            logging.error("Ошибка взятия информации из json")
            logging.exception(e)
            pass

    return top_contracts[:10]
