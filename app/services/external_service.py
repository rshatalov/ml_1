def fetch_employees_from_external_system():
    """
    Заглушка для имитации обращения к внешнему серверу.
    Возвращает фиктивные данные.
    """
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