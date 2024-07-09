# Сироткин Алексей 18яя когорта, Финальный проект. Инженер по тестированию плюс.
import config
import requests
import data


def client_body(body):
    return requests.post(config.URL_SERVER + config.CREATING_OF_ORDER,
                         json=body)


def get_track_number(track_number):
    get_order_url = f"{config.URL_SERVER}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response


def test_auto_creation():
    response = client_body(data.client_body)
    track_number = response.json()["track"]
    print("Ваш заказ создан. Трек-номер вашего заказа:", track_number)

    response_order = get_track_number(track_number)
    assert response_order.status_code == 200, f"ОШИБКА: {response_order.status_code}"
    data_order = response_order.json()
    print("Данные заказа:")
    print(data_order)
