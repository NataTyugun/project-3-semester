import requests #модуль, чтобы получать информацию с сайтов
from dateutil.parser import parse
import sqlite3 #модуль для связи с бд
from icrawler.builtin import GoogleImageCrawler #модуль для получения картинок из гугла
import os

def main(user_city, user_date, user_gender, user_activity):
      global info_weather # в переменной хранится вызов функции, переменнная глобальная для того чтобы вызывать функцую только один раз
      
      city_name = 'спб'
      info_weather = {'app_max_temp': -15.9, 'app_min_temp': -19.3, 'clouds': 42, 'clouds_hi': 20, 'clouds_low': 8, 'clouds_mid': 37, 'datetime': '2023-01-08', 'dewpt': -17, 'high_temp': -12.3, 'low_temp': -13.6, 'max_dhi': None, 'max_temp': -12.3, 'min_temp': -15.3, 'moon_phase': 0.947291, 'moon_phase_lunation': 0.56, 'moonrise_ts': 1673186918, 'moonset_ts': 1673167742, 'ozone': 298.1, 'pop': 0, 'precip': 0, 'pres': 1030.2, 'rh': 79, 'slp': 1032.2, 'snow': 0, 'snow_depth': 117.8, 'sunrise_ts': 1673160988, 'sunset_ts': 1673183934, 'temp': -14, 'ts': 1673125260, 'uv': 1.5, 'valid_date': '2023-01-08', 'vis': 24.128, 'weather': {'description': 'Облачно с прояснениями', 'code': 803, 'icon': 'c03d'}, 'wind_cdir': 'ЮВ', 'wind_cdir_full': 'Юго-Восточный', 'wind_dir': 127, 'wind_gust_spd': 4, 'wind_spd': 1.6}
      #city_name, info_weather = get_weather(user_city, user_date)

      #формируем ответ
      name_city_and_date = f'в городе {city_name} {parse(user_date).strftime("%d.%m.%y").lower()} будет {info_weather["weather"]["description"].lower()}'
      weather = f'средняя температура {round(info_weather["temp"])} C | скорость ветра {round(info_weather["wind_spd"])} м/с'
      recomendation_clouses = f'рекомендуем надеть {get_clouses(user_city, user_date, user_gender, user_activity)[0][0]}'
      other_recomendation_clouses = f'{", ".join(recomendation(user_date, user_city)).lower()}'

      image(user_city, user_date, user_gender, user_activity) #получаем изображения в папку

      return (f'🌎 {name_city_and_date}'
              f'\n🌎 {weather}'
              f'\n🌎 {recomendation_clouses}'
              f'\n🌎 {other_recomendation_clouses}')

# функция для получения информации с сайта погоды, исходя из данных пользователя, возвращает название города и сведения о погоде
def get_weather(user_city, user_date):
      try:
            # с сайта получаем прогноз погоды на 7 дней в введенном городе в формате json, только RU города
            r = requests.get(f'https://api.weatherbit.io/v2.0/forecast/daily?city={user_city},RU&key=3a37beb19b3b4d8981d9e4911cd60f77&lang=ru&days=7').json()
            info = {}  # из 7 дней выбираем тот, который нужен пользователю
            for item in r["data"]:
                  if str(item['datetime']) == user_date:
                        info = item
            print(info)
            return [r["city_name"], info]
      except:
            new_city = input('Введите город занаво: ')
            return get_weather(new_city, user_date)



# функция для рекомендаций исходя из погоды, возвращает особые рекомендации
def recomendation(user_date, user_city):
      # иницилизация переменных, которые хранят дополнительные советы
      rec_wind = ''
      rec_rain = ''
      rec_precip = ''
      rec_uv = ''
      rec_snow = ''
      recomendation = []

      if info_weather['wind_spd'] >= 15:
            rec_wind = 'Не рекоммендуется выходить на улицу из-за сильного ветра'
      elif info_weather['wind_spd'] > 8 and info_weather['wind_spd'] < 15:
            rec_wind = 'Рекомендуется надеть шапку от ветра'

      if info_weather['pop'] > 80 and info_weather['temp'] > 0:
            rec_rain = 'Обязательно возьми зонт или дождевик'
      elif info_weather['pop'] > 30 and info_weather['pop'] < 81 and info_weather['temp'] > 0:
            rec_rain = 'Возможно понадобится зонт'
      elif info_weather['pop'] > 40 and info_weather['temp'] <= 0:
            rec_rain = 'Возможно потребуется очистить машину от снега'

      if info_weather['precip'] > 30:
            rec_precip = 'На улице глубокие лужи, наденьте непромокаемую обувь'

      if  info_weather['uv'] > 4 and info_weather['uv'] < 8:
            rec_uv = 'Используйте spf от 15 и возьмите солнечные очки'
      elif info_weather['uv'] >= 8:
            rec_uv = 'Используйте spf от 30, возьмите солнечные очки и головной убор'

      if info_weather['snow_depth'] >= 200:
            rec_snow = 'Наденьте обувь для высоких сугробов'

      for i in [rec_wind, rec_rain, rec_precip, rec_uv, rec_snow]:
            if i != '':
                  recomendation.append(i)

      return recomendation #выводит особые рекомендации для дня

# функция, которая обращается к БД, в которой хранится подборка одежды, исходя из температуры, возвращает рекомендацию одежды
def get_clouses(user_city, user_date, user_gender, user_activity):
      temp = round(info_weather["temp"])

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

# функция для получения картинок по запросу
def image(user_city, user_date, user_gender, user_activity):

      # получение рекоммендации об одежде
      clouses = get_clouses(user_city, user_date, user_gender, user_activity)

      os.chdir("autfits") # изменение текущего каталога на autfits

      for item in os.listdir(): # удаление страрых папок из папки
            for item2 in os.listdir(item):
                  os.remove(item + '/' + item2)
            os.rmdir(item)

      for item in clouses[0][0].split(','): # Создаем папки
            item = item.strip().replace("/", ", ") # удаляем пробелы и заменяем слеш
            os.mkdir(item) # создаем пустую папку в текущей директори
            os.chdir(item) # изменение текущего каталога на item
            temp_dir = os.getcwd() # запись текущей директории в временную переменную

            google_crawler = GoogleImageCrawler(downloader_threads=1, storage={'root_dir': temp_dir})  # добавляем в текущую папку изображения, storage - расположение папки итогового хранения изображений
            google_crawler.crawl(keyword=f'{"женские" if user_gender == "ж" else "мужские"} {item}', max_num=1)  #keyword - запрос в гугл изсображения, max_num - количество скачиваемых изображений

            os.chdir("..") # возврвщаемся в autfits

      os.chdir("..")
      return

#данные пользователя
user_city= input('Введите город: ')
user_date = parse(input('Введите дату (прогноз на 7 дней!): ')).strftime('%Y-%d-%m')
user_gender = input('Выберите м\ж: ')
user_activity = input('Выберите прогулка\спорт\ежедневные дела: ')

#вызов главной функции от информации пользователя
print(main(user_city, user_date, user_gender, user_activity))
