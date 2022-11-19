import requests #модуль, чтобы получать информацию с сайтов
from dateutil.parser import parse
import json
import sqlite3

#данные пользователя
user_city = input('Введите город: ')
user_data = parse(input('Введите дату (прогноз на 7 дней!): ')).strftime('%Y-%m-%d')
user_gender = input('Вымерите м\ж: ')
user_activity = input('Выберите прогулка\спорт\ежедневные дела: ')

# с сайта получаем прогноз погоды на 7 дней в введенном городе
r = requests.get(f'https://api.weatherbit.io/v2.0/forecast/daily?city={user_city},RU&key=3a37beb19b3b4d8981d9e4911cd60f77&lang=ru&days=7').json()

# из 7 дней выбираем тот, который нужен пользователю
info_weather = {}
for item in r["data"]:
    if str(item['valid_date']) == user_data:
        info_weather = item

# функция для вывода информации о погоде, тут можно посмотреть на ключи значений
def get_weather(info_weather, r, user_data):
      return print(f'\n В городе {r["city_name"]} {parse(user_data).strftime("%d %B")} {info_weather["weather"]["description"]}'
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

#иницилизация переменных, которые хранят дополнительные советы
rec_wind = ''
rec_rain = ''
rec_precip = ''
rec_uv = ''
rec_snow = ''

# функция для рекомендаций исходя из погоды
def recomendation(info_weather, rec_wind, rec_rain, rec_precip, rec_uv, rec_snow):
      if info_weather['wind_spd'] >= 15:
            rec_wind = 'Не рекоммендуется выходить на улицу из-за сильного ветра'
      elif info_weather['wind_spd'] > 8 and info_weather['wind_spd'] < 15:
            rec_wind = 'На улице ветер, рекомендуется надеть шапку'
      else:
            rec_wind = ''

      if info_weather['pop'] > 80:
            rec_rain = 'Обязательно возьми зонт или дождевик'
      elif info_weather['pop'] > 30 and info_weather['pop'] < 81:
            rec_rain = 'Возможно сегодня понадобится зонт'
      else:
            rec_rain = ''

      if info_weather['precip'] > 30:
            rec_precip = 'На улице глубокие лужи, наденьте непромокаемую обувь'
      else:
            rec_precip = ''

      if  info_weather['uv'] > 4 and info_weather < 8:
            rec_uv = 'На улице солнечно, используйте spf от 15 и возьмите солнечные очки'
      elif info_weather['uv'] >= 8:
            rec_uv = 'На улице сильное солнце, используйте spf от 30, возьмите солнечные очки и головной убор'
      else:
            rec_uv = ''

      if info_weather['snow_depth'] >= 200:
            rec_snow = 'На улице глубокие сугробы, наденьте высокую обувь'
      else:
            rec_snow = ''

      return (rec_wind, rec_rain, rec_precip, rec_uv, rec_snow) #выводит особые рекомендации для дня

# функция, которая обращается к БД, в которой хранится подборка одежды, исходя из температуры
def get_clouses(temp, user_gender, user_activity):

      connect = sqlite3.connect('database_new.db')  #делаем запрос к базе данных
      cursor = connect.cursor()

      if user_gender == 'ж':
            if user_activity == 'спорт':
                  cursor.execute('''SELECT female_sport FROM database_new WHERE temp = ?''', [temp])
                  recomendation_clouses = cursor.fetchall()
                  connect.close()
            if user_activity == 'прогулка':
                  cursor.execute('''SELECT female_walk FROM database_new WHERE temp = ?''', [temp])
                  recomendation_clouses = cursor.fetchall()
                  connect.close()
            if user_activity == 'ежедневные дела':
                  cursor.execute('''SELECT female_day FROM database_new WHERE temp = ?''', [temp])
                  recomendation_clouses = cursor.fetchall()
                  connect.close()

      if user_gender == 'м':
            if user_activity == 'спорт':
                  cursor.execute('''SELECT male_sport FROM database_new WHERE temp = ?''', [temp])
                  recomendation_clouses = cursor.fetchall()
                  connect.close()
            if user_activity == 'прогулка':
                  cursor.execute('''SELECT male_walk FROM database_new WHERE temp = ?''', [temp])
                  recomendation_clouses = cursor.fetchall()
                  connect.close()
            if user_activity == 'ежедневные дела':
                  cursor.execute('''SELECT male_day FROM database_new WHERE temp = ?''', [temp])
                  recomendation_clouses = cursor.fetchall()
                  connect.close()

      return recomendation_clouses



#print(get_weather(info_weather, r, user_data))
#print(recomendation(info_weather, rec_wind, rec_rain, rec_precip, rec_uv, rec_snow))
print(f'{user_data} рекомендуем надеть {get_clouses(round(info_weather["temp"]), user_gender, user_activity)}')
#print(type(get_clouses(round(info_weather["temp"]), user_gender, user_activity))[0])
