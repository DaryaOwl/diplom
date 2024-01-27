import configuration
import requests

# создание заказа
def create_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

# получение информации о заказе по треку
def get_order_number_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_NUMBER + str(track))