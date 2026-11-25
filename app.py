import aiohttp


async def get_json(url):
    # Создаем асинхронный клиент для HTTP-запросов
    async with aiohttp.ClientSession() as session:
        # Отправляем GET-запрос по URL
        async with session.get(url) as response:
            # Проверяем статус ответа
            if response.status == 200:
                # Читаем данные из ответа в формате JSON
                data = await response.json()
                # Возвращаем данные
                return data
            else:
                # Возвращаем None в случае ошибки
                return None