import requests
from dateutil.parser import parse

user_city = input('Введите город: ')
user_data = parse(input('Введите дату (прогноз на 7 дней!): ')).strftime('%Y-%m-%d')

r = requests.get(f'https://api.weatherbit.io/v2.0/forecast/daily?city={user_city},RU&key=3a37beb19b3b4d8981d9e4911cd60f77&lang=ru&days=7').json()
info_weather = {}

for item in r["data"]:
    if str(item['valid_date']) == user_data:
        info_weather = item

print(f'\n В городе {r["city_name"]} {user_data} {info_weather["weather"]["description"].lower()}'
      f'\n Средняя температура {info_weather["temp"]} C'
      f'\n Макс температура {info_weather["max_temp"]} C'
      f'\n Мин температура {info_weather["min_temp"]} C'
      f'\n Ощущается как {info_weather["app_min_temp"]} - {info_weather["app_max_temp"]} C'
      f'\n Скорость ветра {info_weather["wind_spd"]} m/c' 
      f'\n Вероятность осадков {info_weather["pop"]} % ' 
      f'\n Влажность {info_weather["rh"]} %'
      f'\n Глубина луж {info_weather["precip"]} мм'
      f'\n Снег {info_weather["snow"]} мм'
      f'\n Глубина снега {info_weather["snow_depth"]} мм'
      f'\n УФ индекс {info_weather["uv"]}'
      )
