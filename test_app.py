import pytest  
import allure  
from app import get_json  

# Тест, который проверяет, что функция возвращает корректный JSON-ответ от API погоды  
@pytest.mark.asyncio  
@allure.feature("JSON response")  
@allure.story("Weather API")  
@allure.title("Test get_json with weather API")  
@allure.description("This test checks that the get_json function returns a correct JSON  response from the weather API.")  
@allure.severity(allure.severity_level.NORMAL)  
@allure.tag("json", "api", "weather")  
async def test_get_json_weather():  
    # URL для API погоды  
    url = "https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=c5628d520368633b9bbc57246065a2ec"  
    # Ожидаемый результат  
    expected = {
  "coord": {
    "lon": 37.6156,
    "lat": 55.7522
  },
  "weather": [
    {
      "id": 600,
      "main": "Snow",
      "description": "light snow",
      "icon": "13d"
    }
  ],
    "base": "stations",
    "main": {
        "temp": 273.03,
        "feels_like": 268.14,
        "temp_min": 272.39,
        "temp_max": 273.92,
        "pressure": 1000,
        "humidity": 67,
        "sea_level": 1000,
        "grnd_level": 982
    },
  "visibility": 10000,
  "wind": {
    "speed": 4.9,
    "deg": 359,
    "gust": 10.83
  },
  "snow": {
    "1h": 0.18
  },
  "clouds": {
    "all": 100
  },
  "dt": 1795601545,
  "sys": {
    "type": 2,
    "id": 2095214,
    "country": "RU",
    "sunrise": 1795584242,
    "sunset": 1795612153
  },
  "timezone": 10800,
  "id": 524901,
  "name": "Moscow",
  "cod": 200
}
@pytest.mark.asyncio  
async def test_get_json_weer(): 
        
    url = "https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=c5628d520368633b9bbc57246065a2ec"
        
    expected = {
          "coord": {
            "lon": 37.6156,
            "lat": 55.7522
          },
          "weather": [
            {
              "id": 600,
              "main": "Snow",
              "description": "light snow",
              "icon": "13d"
            }
          ],
          "base": "stations",
            "main": {
              "temp": 273.03,
              "feels_like": 268.14,
              "temp_min": 272.39,
              "temp_max": 273.92,
              "pressure": 1000,
              "humidity": 67,
              "sea_level": 1000,
              "grnd_level": 982
            }
        }
@pytest.mark.asyncio      
async def test_get_json_ther(): 
            
    url = "https://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=c5628d520368633b9bbc57246065a2ec"
            
    expected = {
                 "timezone": 10800,
                   "id": 524901,
                   "name": "Moscow",
                   "cod": 200
            }
    
    # Вызываем функцию с URL  
    result = await get_json(url)  
    # Проверяем, что результат не None  
    assert result is not None  
    # Проверяем, что результат совпадает с ожидаемым  
    assert result == expected