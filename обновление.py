import requests #модуль, чтобы получать информацию с сайтов
from dateutil.parser import parse
import sqlite3 #модуль для связи с бд
from icrawler.builtin import GoogleImageCrawler #модуль для получения картинок из гугла
import os

def main():
      #данные пользователя

      user_city = input('Введите город: ')
      user_data = parse(input('Введите дату (прогноз на 7 дней!): ')).strftime('%Y-%m-%d')
      user_gender = input('Выберите м\ж: ')
      user_activity = input('Выберите прогулка\спорт\ежедневные дела: ')

      city_name = get_weather(user_city, user_data)[0]
      info_weather = get_weather(user_city, user_data)[1]

      image(user_city, user_data, user_gender, user_activity)

      return (f'🌎 В городе {city_name} {parse(user_data).strftime("%d.%m.%y").lower()} будет {info_weather["weather"]["description"].lower()}'
              f'\n🌎 Средняя температура {round(info_weather["temp"])} C | скорость ветра {round(info_weather["wind_spd"])} м/с '
              f'\n🌎 Рекомендуем надеть {get_clouses(user_city, user_data, user_gender, user_activity)[0][0]}'
              f'\n{recomendation(user_data, user_city)}')


# функция для получения информации с сайта погоды, исходя из данных пользователя, возвращает название города и сведения о погоде

def get_weather(user_city, user_data):
      r = requests.get(f'https://api.weatherbit.io/v2.0/forecast/daily?city={user_city},RU&key=3a37beb19b3b4d8981d9e4911cd60f77&lang=ru&days=7').json() # с сайта получаем прогноз погоды на 7 дней в введенном городе в формате json, ттолько RU города

      info_weather = {} # из 7 дней выбираем тот, который нужен пользователю
      for item in r["data"]:
            if str(item['valid_date']) == user_data:
                  info_weather = item

      return [r["city_name"], info_weather]

# функция для вывода информации о погоде, тут можно посмотреть на ключи и значения, возвращает краткие сведения о погоде

def look_weather(user_data, user_city, user_gender, user_activity):
      #print(f'\n В городе {city_name} {parse(user_data).strftime("%d %B")} {info_weather["weather"]["description"]}'
      #      f'\n Средняя температура {info_weather["temp"]} C'
      #      f'\n Макс температура {info_weather["max_temp"]} C'
      #      f'\n Мин температура {info_weather["min_temp"]} C'
      #      f'\n Ощущается как {info_weather["app_min_temp"]} - {info_weather["app_max_temp"]} C'
      #      f'\n Скорость ветра {info_weather["wind_spd"]} m/c'
      #      f'\n Вероятность осадков {info_weather["pop"]} % '
      #      f'\n Влажность {info_weather["rh"]} %'
      #      f'\n Глубина луж {info_weather["precip"]} мм'
      #      f'\n Снег {info_weather["snow"]} мм'
      #      f'\n Глубина снега {info_weather["snow_depth"]} мм'
      #      f'\n УФ индекс {info_weather["uv"]}'
      #      )

      return

# функция для рекомендаций исходя из погоды, возвращает особые рекомендации

def recomendation(user_data, user_city):
      info_weather = get_weather(user_city, user_data)[1]

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
            rec_wind = 'На улице ветер, рекомендуется надеть шапку'

      if info_weather['pop'] > 80:
            rec_rain = 'Обязательно возьми зонт или дождевик'
      elif info_weather['pop'] > 30 and info_weather['pop'] < 81:
            rec_rain = 'Возможно сегодня понадобится зонт'

      if info_weather['precip'] > 30:
            rec_precip = 'На улице глубокие лужи, наденьте непромокаемую обувь'

      if  info_weather['uv'] > 4 and info_weather < 8:
            rec_uv = 'На улице солнечно, используйте spf от 15 и возьмите солнечные очки'
      elif info_weather['uv'] >= 8:
            rec_uv = 'На улице сильное солнце, используйте spf от 30, возьмите солнечные очки и головной убор'

      if info_weather['snow_depth'] >= 200:
            rec_snow = 'На улице глубокие сугробы, наденьте высокую обувь'

      for i in [rec_wind, rec_rain, rec_precip, rec_uv, rec_snow]:
            if i != '':
                  recomendation.append(i)

      return recomendation #выводит особые рекомендации для дня

# функция, которая обращается к БД, в которой хранится подборка одежды, исходя из температуры, возвращает рекомендацию одежды

def get_clouses(user_city, user_data, user_gender, user_activity):
      temp = round(get_weather(user_city, user_data)[1]["temp"])

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

def image(user_city, user_data, user_gender, user_activity):

      # удаление страрых фотографий из папки
      dir = os.getcwd()+'\autfits'
      for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

      # получение рекоммендации об одежде
      clouses = get_clouses(user_city, user_data, user_gender, user_activity)

      for item in (clouses[0][0].split(",")):
            # Создаем папки, если их нет
            os.mkdir(item)

            temp_dir = f'{dir}\{item.strip()}'

            google_crawler = GoogleImageCrawler(downloader_threads=4, storage={'root_dir': temp_dir})  ##storage - расположениt папки итогового хранения изображений
            google_crawler.crawl(keyword=f'{"женщина" if user_gender == "ж" else "мужчина"}' + item, max_num=3)  ##keyword - запрос в гугл изсображения, max_num - количество скачиваемых изображений

      return 'Изображение в папке!'

print(main())
