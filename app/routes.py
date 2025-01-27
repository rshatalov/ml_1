from flask import Blueprint, jsonify
from app.services.external_service import fetch_employees_from_external_system

main_routes = Blueprint('main', __name__)

@main_routes.route('/team/get_employees', methods=['GET'])
def get_employees():
    try:
        # Получаем данные из заглушки
        data = fetch_employees_from_external_system()

        # Преобразуем данные в нужный формат
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

        return jsonify(employees)

    except Exception as e:
        return jsonify({'error': str(e)}), 500