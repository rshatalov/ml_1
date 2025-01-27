from flask import Blueprint, jsonify
from app.services.external_service import fetch_employees_from_external_system

main_routes = Blueprint('main', __name__)

@app.route("/team/get_employees", methods=["GET"])
async def get_employees():
    # Получаем данные из внешнего сервиса
    data = await fetch_employees_from_1c()

    # Если внешний сервис недоступен, используем заглушку
    if data is None:
        print("Используем заглушку, так как внешний сервис недоступен")
        data = fetch_employees_from_external_system()

    # Преобразуем данные в нужный формат
    employees = []
    for emp in data.get("Specialists", []):
        employee = {
            "id": emp.get("Id", ""),
            "name": emp.get("FirstName", ""),
            "last_name": emp.get("LastName", ""),
            "phone": emp.get("Phone", ""),
            "image_url": emp.get("ImageUrl", ""),
        }
        employees.append(employee)

    return jsonify(employees)