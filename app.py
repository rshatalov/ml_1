from flask import Flask, jsonify, request, Response
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

# Конфигурационные параметры
CONFIG = {
    '1C_URL': 'http://176.192.70.122:90/fitnes_t_nfc_mobile/hs/nfc_mobile/v1',
    '1C_LOGIN': 'FitnessKit',
    '1C_PASSWORD': 'vY0xodyg',
    'CLUB_ID': '59115d1e-9052-11eb-810c-6eae8b56243b',
    'REQUEST_ID': 'e1477272-88d1-4acc-8e03-7008cdedc81e'
}

def fetch_employees_from_external_system(login, password, payload):
    """
    Заглушка функции для обращения к внешнему серверу.
    Возвращает фиктивные данные, если внешний сервер недоступен.
    """
    # Пример фиктивных данных
    mock_data = {
        "Specialists": [
            {
                "Id": "123",
                "FirstName": "Иван",
                "LastName": "Иванов",
                "Phone": "+71234567890",
                "ImageUrl": "http://example.com/image1.jpg"
            },
            {
                "Id": "124",
                "FirstName": "Петр",
                "LastName": "Петров",
                "Phone": "+79876543210",
                "ImageUrl": ""
            }
        ]
    }
    return mock_data


@app.route('/team/get_employees', methods=['GET'])
def get_employees():
    # Выполнение запроса к 1С
    try:
        payload = {
            "Request_id": CONFIG['REQUEST_ID'],
            "ClubId": CONFIG['CLUB_ID'],
            "Method": "GetSpecialistList",
            "Parameters": {
                "ServiceId": ""
            }
        }

        data = fetch_employees_from_external_system(CONFIG['1C_LOGIN'], CONFIG['1C_PASSWORD'], payload)

        # Преобразование данных
        employees = []
        for emp in data.get('Specialists', []):
            employee = {
                'id': emp.get('Id', ''),
                'name': emp.get('FirstName', ''),
                'last_name': emp.get('LastName', ''),
                'phone': emp.get('Phone', ''),
                'image_url': emp.get('ImageUrl', '')
            }
            employees.append(employee)
        response = Response(
            json.dumps(data, ensure_ascii=False),
            content_type='application/json; charset=utf-8'
        )
        return response

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)