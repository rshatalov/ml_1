import httpx
from httpx import HTTPStatusError


async def fetch_employees_from_1c():
    """
    Выполняет запрос к внешнему сервису 1С.
    """
    payload = {
        "Request_id": CONFIG["REQUEST_ID"],
        "ClubId": CONFIG["CLUB_ID"],
        "Method": "GetSpecialistList",
        "Parameters": {"ServiceId": ""},
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                CONFIG["1C_URL"],
                json=payload,
                auth=(CONFIG["1C_LOGIN"], CONFIG["1C_PASSWORD"]),
            )
            response.raise_for_status()  # Проверяем статус ответа
            return response.json()
    except HTTPStatusError as e:
        print(f"Ошибка при запросе к 1С: {e}")
        return None