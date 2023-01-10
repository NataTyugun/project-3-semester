import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from functools import partial
from tkinter import messagebox
import requests  # модуль, чтобы получать информацию с сайтов
from dateutil.parser import parse
import sqlite3  # модуль для связи с бд
from icrawler.builtin import GoogleImageCrawler  # модуль для получения картинок из гугла
import os

"""
Блок маленьких функций для интерфейса
"""

# функция для кнопки "закрыть"
def closed(win):
    win.destroy()

    
# функция для открытия первого окна 
def open_first(win_close):
    win_close.destroy()
    first_window()

# функция для открытия второго окна
def open_second(win_close):
    win_close.destroy()
    second_window()


# функция для открытия третьего окна    
def open_third(win_close):
    win_close.destroy()
    third_window()


# функция для кнопки активности "спорт"
def sport():
    activity = 'спорт'
    print(activity)
    return activity

# функция для кнопки активности "прогулка"
def walk():
    activity = 'прогулка'
    print(activity)
    return activity


# функция для кнопки активности "дела"
def work():
    activity = 'ежедневные дела'
    print(activity)
    return activity


# функция для информации в третьем окне
def info(user_date, user_city):
    user_info = user_date + '  ' + user_city
    return user_info


"""
Первое окно интерфейса, ввод города пользователя 
"""


def first_window():
    # необходимая глобальная переменная 
    global city
    
    # создание окна
    window_first = Tk()
    window_first.title('WEATHER_CITY')
    window_first.geometry("300x300")
    window_first['bg'] = 'lavender'
     
    # картинка в первом окне
    canvas = Canvas(window_first, width=80, height=60, bg='lavender')
    oblaco = PhotoImage(file='oblaco.png')
    canvas.create_image(20, 20, anchor=NW, image=oblaco)

    # переменные для ввода данных
    city = StringVar()

    # блок невидимых рамок для красивого интерфейса
    f_0 = Frame(window_first)
    f_1 = Frame(window_first)
    f_2 = Frame(window_first)
    f_3 = Frame(window_first)
    
    # ввод данных
    label = Label(f_0, text="ПРОГНОЗ ОДЕЖДЫ", bg="lavender", fg='midnightblue', font='Arial 20 underline', width=30,
                  height=1)
    
    label_1 = Label(f_1, text="ВВЕДИТЕ ВАШ ГОРОД", bg="lavender", fg='midnightblue', font=70, width=30, height=1)

    city_entry = Entry(f_2, width=70, textvariable=city)

    close_button = Button(window_first, text="ЗАКРЫТЬ", bg="pink", command=partial(closed, window_first), width=15,
                          height=1)

    next_button = Button(window_first, text="ПРОДОЛЖИТЬ", bg="pink", command=partial(open_second, window_first),
                         width=15, height=1)

    # упорядочивание элементов окна
    f_0.pack(pady=1, expand=1)
    canvas.pack(pady=5, expand=1)
    f_1.pack(pady=3, expand=1)
    f_2.pack(pady=5, expand=1)
    f_3.pack(pady=7)
    close_button.pack(anchor=W)
    next_button.pack(anchor=E)

    label_1.pack(side=LEFT)
    label.pack(side=LEFT)
    close_button.pack(side=LEFT)
    next_button.pack(side=RIGHT)
    city_entry.pack(side=LEFT)

    window_first.mainloop()

    return city


'''
Второе окно интерфейса, ввод даты, пола и активности пользователя
'''
def second_window():
    # необходимые глобальные переменные 
    global date, gender, activity
    
    # создание окна
    window_second = Tk()
    window_second.title('WEATHER_RESULT')
    window_second.geometry("500x400")
    window_second['bg'] = 'lavender'

    # переменные для ввода данных
    date = StringVar()
    gender = StringVar()
    activity = StringVar()

    # блок невидимых рамок для красивого интерфейса
    f_0 = Frame(window_second)
    f_1 = Frame(window_second)
    f_2 = Frame(window_second)
    f_3 = Frame(window_second)
    f_4 = Frame(window_second, bg='lavender')
    f_5 = Frame(window_second)
    f_6 = Frame(window_second, bg='lavender')

    # ввод данных

    label = Label(f_0, text="ПОЛЬЗОВАТЕЛЬСКАЯ ИНФОРМАЦИЯ", bg="lavender", fg='midnightblue',
                  font=(' Arial 20 underline'), width=40, height=1)

    label_1 = Label(f_1, text="ДАТА", bg="lavender", fg='midnightblue', font=70, width=40, height=1)
    date_entry = Entry(f_2, width=8, textvariable=date)

    label_2 = Label(f_3, text="ПОЛ", bg="lavender", fg='midnightblue', font=70, width=30, height=1)

    rad1 = Radiobutton(f_4, text='М', value=4, variable=gender)
    rad2 = Radiobutton(f_4, text='Ж', value=-161, variable=gender)

    label_3 = Label(f_5, text="ДЕЯТЕЛЬНОСТЬ", bg="lavender", fg='midnightblue', font=70, width=30, height=1)

    walk_button = Button(f_6, text="прогулка", bg="pink", command=lambda: walk(), width=12, height=2)
    sport_button = Button(f_6, text="спорт ", bg="pink", command=lambda: sport(), width=12, height=2)
    work_button = Button(f_6, text="дела", bg="pink", command=lambda: work(), width=12, height=2)

    last_button = Button(window_second, text="НАЗАД", bg="pink", command=partial(open_first, window_second), width=15,
                         height=1)
    next_button = Button(window_second, text="ПРОДОЛЖИТЬ", bg="pink", command=partial(open_third, window_second),
                         width=15, height=1)

    # упорядочивание элементов окна
    f_0.pack(pady=5, expand=1)
    f_1.pack(pady=5, expand=1)
    f_2.pack(pady=5, expand=1)
    f_3.pack(pady=5, expand=1)
    f_4.pack(pady=5, expand=1)
    f_5.pack(pady=5, expand=1)
    f_6.pack(pady=5, expand=1)
    last_button.pack(anchor=W)
    next_button.pack(anchor=E)
    walk_button.pack(pady=5, expand=1)
    sport_button.pack(pady=5, expand=1)
    work_button.pack(pady=5, expand=1)

    label_1.pack(side=LEFT)
    label.pack(side=LEFT)
    label_2.pack(side=LEFT)
    label_3.pack(side=LEFT)
    rad1.pack(side=LEFT)
    rad2.pack(side=LEFT)
    last_button.pack(side=LEFT)
    next_button.pack(side=RIGHT)
    walk_button.pack(side=LEFT)
    sport_button.pack(side=LEFT)
    work_button.pack(side=LEFT)
    date_entry.pack(side=LEFT)

    window_second.mainloop()

    return date, gender, activity

# пример рекомендации для вывода в окне 3
recom = 'не забудьте надеть трусы'

'''
Третье окно интерфейса, итоги программы, вывод даты, города и соответствующих рекомендаций по одежде 
'''
def third_window():
  
    # создание окна
    window_third = Tk()
    window_third.title('WEATHER_INFO')
    window_third.geometry("500x500")
    window_third['bg'] = 'lavender'

    # блок невидимых рамок для красивого интерфейса
    f_0 = Frame(window_third)
    f_1 = Frame(window_third)
    f_2 = Frame(window_third)
    f_3 = Frame(window_third)
    f_4 = Frame(window_third)
    f_5 = Frame(window_third)

    # ввод данных

    label = Label(f_0, text=info(date.get(), city.get()), bg="lavender", fg='midnightblue', font=90, width=30, height=1)
    label_1 = Label(f_1, text="ПОГОДА", bg="lavender", fg='midnightblue', font=70, width=30, height=1)
    label_2 = Label(f_3, text=recom, bg="lavender", fg='midnightblue', font=70, width=30, height=1)
    label_3 = Label(f_4, text="ПРИМЕР ОДЕЖДЫ", bg="lavender", fg='midnightblue', font=70, width=30, height=1)
    recomendation_entry = Entry(f_5, width=70)

    last_button = Button(window_third, text="НАЗАД", bg="pink", command=partial(open_second, window_third), width=15,
                         height=1)
    next_button = Button(window_third, text="ЗАКРЫТЬ", bg="pink", command=partial(closed, window_third), width=15,
                         height=1)

    # упорядочивание элементов окна
    f_0.pack(pady=5)
    f_1.pack(pady=5)
    f_2.pack(pady=5)
    f_3.pack(pady=5)
    f_4.pack(pady=5)
    f_5.pack(pady=5)
    last_button.pack(anchor=SW)
    next_button.pack(anchor=SE)
    last_button.pack(side=LEFT)
    next_button.pack(side=RIGHT)

    label.pack(side=LEFT)
    label_1.pack(side=LEFT)
    label_2.pack(side=LEFT)
    label_3.pack(side=LEFT)
    recomendation_entry.pack(side=LEFT, expand=1)

    window_third.mainloop()


def main(user_city, user_date, user_gender, user_activity):
    global info_weather  # в переменной хранится вызов функции, переменнная глобальная для того чтобы вызывать функцую только один раз

    # city_name = 'спб'
    # info_weather = {'app_max_temp': -15.9, 'app_min_temp': -19.3, 'clouds': 42, 'clouds_hi': 20, 'clouds_low': 8,
    #               'clouds_mid': 37, 'datetime': '2023-01-08', 'dewpt': -17, 'high_temp': -12.3, 'low_temp': -13.6,
    #               'max_dhi': None, 'max_temp': -12.3, 'min_temp': -15.3, 'moon_phase': 0.947291,
    #               'moon_phase_lunation': 0.56, 'moonrise_ts': 1673186918, 'moonset_ts': 1673167742, 'ozone': 298.1,
    #               'pop': 0, 'precip': 0, 'pres': 1030.2, 'rh': 79, 'slp': 1032.2, 'snow': 0, 'snow_depth': 117.8,
    #               'sunrise_ts': 1673160988, 'sunset_ts': 1673183934, 'temp': -14, 'ts': 1673125260, 'uv': 1.5,
    #               'valid_date': '2023-01-08', 'vis': 24.128,
    #               'weather': {'description': 'Облачно с прояснениями', 'code': 803, 'icon': 'c03d'},
    #               'wind_cdir': 'ЮВ', 'wind_cdir_full': 'Юго-Восточный', 'wind_dir': 127, 'wind_gust_spd': 4,
    #               'wind_spd': 1.6}
    city_name, info_weather = get_weather(user_city, user_date)

    # формируем ответ
    name_city_and_date = f'в городе {city_name} {parse(user_date).strftime("%d.%m.%y").lower()} будет {info_weather["weather"]["description"].lower()}'
    weather = f'средняя температура {round(info_weather["temp"])} C | скорость ветра {round(info_weather["wind_spd"])} м/с'
    recomendation_clouses = f'рекомендуем надеть {get_clouses(user_city, user_date, user_gender, user_activity)[0][0]}'
    other_recomendation_clouses = f'{", ".join(recomendation(user_date, user_city)).lower()}'

    image(user_city, user_date, user_gender, user_activity)  # получаем изображения в папку

    return (f'🌎 {name_city_and_date}'
            f'\n🌎 {weather}'
            f'\n🌎 {recomendation_clouses}'
            f'\n🌎 {other_recomendation_clouses}')


# функция для получения информации с сайта погоды, исходя из данных пользователя, возвращает название города и сведения о погоде
def get_weather(user_city, user_date):
    try:
        # с сайта получаем прогноз погоды на 7 дней в введенном городе в формате json, только RU города
        r = requests.get(
            f'https://api.weatherbit.io/v2.0/forecast/daily?city={user_city},RU&key=3a37beb19b3b4d8981d9e4911cd60f77&lang=ru&days=7').json()
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
    rec_wind = ''
    rec_rain = ''
    rec_precip = ''
    rec_uv = ''
    rec_snow = ''
    recomendation = []

    if info_weather['wind_spd'] >= 15:
        rec_wind = 'Не рекоммендуется выходить на улицу из-за сильного ветра'
    elif 8 < info_weather['wind_spd'] < 15:
        rec_wind = 'Рекомендуется надеть шапку от ветра'

    if info_weather['pop'] > 80 and info_weather['temp'] > 0:
        rec_rain = 'Обязательно возьми зонт или дождевик'
    elif 30 < info_weather['pop'] < 81 and info_weather['temp'] > 0:
        rec_rain = 'Возможно понадобится зонт'
    elif info_weather['pop'] > 40 and info_weather['temp'] <= 0:
        rec_rain = 'Возможно потребуется очистить машину от снега'

    if info_weather['precip'] > 30:
        rec_precip = 'На улице глубокие лужи, наденьте непромокаемую обувь'

    if 4 < info_weather['uv'] < 8:
        rec_uv = 'Используйте spf от 15 и возьмите солнечные очки'
    elif info_weather['uv'] >= 8:
        rec_uv = 'Используйте spf от 30, возьмите солнечные очки и головной убор'

    if info_weather['snow_depth'] >= 200:
        rec_snow = 'Наденьте обувь для высоких сугробов'

    for i in [rec_wind, rec_rain, rec_precip, rec_uv, rec_snow]:
        if i != '':
            recomendation.append(i)

    return recomendation  # выводит особые рекомендации для дня


# функция, которая обращается к БД, в которой хранится подборка одежды, исходя из температуры, возвращает рекомендацию одежды
def get_clouses(user_city, user_date, user_gender, user_activity):
    temp = round(info_weather["temp"])

    connect = sqlite3.connect('database_new.db')  # делаем запрос к базе данных
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

    os.chdir("autfits")  # изменение текущего каталога на autfits

    for item in os.listdir():  # удаление страрых папок из папки
        for item2 in os.listdir(item):
            os.remove(item + '/' + item2)
        os.rmdir(item)

    for item in clouses[0][0].split(','):  # Создаем папки
        item = item.strip().replace("/", ", ")  # удаляем пробелы и заменяем слеш
        os.mkdir(item)  # создаем пустую папку в текущей директори
        os.chdir(item)  # изменение текущего каталога на item
        temp_dir = os.getcwd()  # запись текущей директории в временную переменную

        google_crawler = GoogleImageCrawler(downloader_threads=1, storage={
            'root_dir': temp_dir})  # добавляем в текущую папку изображения, storage - расположение папки итогового хранения изображений
        google_crawler.crawl(keyword=f'{"женские" if user_gender == "ж" else "мужские"} {item}',
                             max_num=1)  # keyword - запрос в гугл изсображения, max_num - количество скачиваемых изображений

        os.chdir("..")  # возврвщаемся в autfits

    os.chdir("..")
    return


# данные пользователя

# user_date = parse(input('Введите дату (прогноз на 7 дней!): ')).strftime('%Y-%d-%m')
# user_gender = input('Выберите м\ж: ')
# user_activity = input('Выберите прогулка\спорт\ежедневные дела: ')

# вызов главной функции от информации пользователя
# print(main(user_city, user_date, user_gender, user_activity))


# старт программы с вызова первого окна
first_window()
