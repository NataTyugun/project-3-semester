import sqlite3
from tkinter.ttk import Radiobutton, Combobox
from functools import partial
from tkinter import messagebox
import requests
from dateutil.parser import parse
from icrawler.builtin import GoogleImageCrawler
import os
from tkinter import *
import os.path
from PIL import ImageTk, Image
import datetime

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

"""
Первое окно интерфейса, ввод города пользователя 
"""

global city
def first_window():
    global city

    # создание окна
    window_first = Tk()
    window_first.title('WEATHER_CITY')
    window_first.geometry("400x250")
    window_first['bg'] = "AliceBlue"

    # картинка в первом окне
    canvas = Canvas(window_first, width=55, height=40, bg="AliceBlue")
    oblaco = PhotoImage(file='oblaco.png')
    canvas.create_image(10, 10, anchor=NW, image=oblaco)

    # переменные для ввода данных
    city = StringVar()

    # блок невидимых рамок для красивого интерфейса
    f_0 = Frame(window_first)
    f_1 = Frame(window_first)
    f_2 = Frame(window_first)
    f_3 = Frame(window_first)

    # ввод данных
    label = Label(f_0, text="ПРОГНОЗ ОДЕЖДЫ", bg="AliceBlue", fg="CornflowerBlue", font='Helvetica 18 bold')
    label.pack(side=LEFT)

    label_1 = Label(f_1, text="город для прогноза", bg="AliceBlue", fg="CornflowerBlue", font=40)
    label_1.pack(side=LEFT)

    city_entry = Entry(f_2, width=50, textvariable=city)

    close_button = Button(window_first, text="ЗАКРЫТЬ", bg="Pink", fg="HotPink4", command=partial(closed, window_first),
                          width=15,
                          height=1)

    city_entry.pack(side=LEFT)

    next_button = Button(window_first, text="ПРОДОЛЖИТЬ", bg="pink", fg="HotPink4",
                         command=partial(open_second, window_first),
                         width=15, height=1)

    # упорядочивание элементов окна
    f_0.pack(expand=1)
    canvas.pack(expand=1)
    f_1.pack(expand=1)
    f_2.pack(expand=1)
    f_3.pack(pady=4, expand=1)

    close_button.pack(anchor=W)
    next_button.pack(anchor=E)

    close_button.pack(side=LEFT)
    next_button.pack(side=RIGHT)

    window_first.mainloop()

    return

'''
Второе окно интерфейса, ввод даты, пола и активности пользователя
'''

global date, gender, activity
def second_window():
    # необходимые глобальные переменные
    global date, gender, activity
    
    try:
        get_weather(city.get(), str(datetime.datetime.now()))
    except:
        messagebox.showerror('ОШИБКА', 'Город введен неправильно')
        first_window()
        return
    
    # создание окна
    window_second = Tk()
    window_second.title('WEATHER_INFO')
    window_second.geometry("400x250")
    window_second['bg'] = "AliceBlue"

    # переменные для ввода данных
    date = StringVar()
    gender = StringVar()
    activity = StringVar()

    # блок невидимых рамок для красивого интерфейса
    f_0 = Frame(window_second, bg="AliceBlue")
    f_1 = Frame(window_second, bg="AliceBlue")
    f_2 = Frame(window_second, bg="AliceBlue")
    f_3 = Frame(window_second, bg="AliceBlue")
    f_4 = Frame(window_second, bg="AliceBlue")

    # ввод данных
    label = Label(f_0, text="ИНФОРМАЦИЯ О ВАС", bg="AliceBlue", fg="CornflowerBlue", font='Helvetica 18 bold')
    label.pack()

    label_1 = Label(f_1, text="дата прогноза", bg="AliceBlue", fg="CornflowerBlue", font=40)
    date_entry = Entry(f_1, width=10, textvariable=date)
    label_1.pack(side=LEFT, padx=6)
    date_entry.pack(side=LEFT)

    label_2 = Label(f_2, text="пол", bg="AliceBlue", fg="CornflowerBlue", font=40)
    rad1 = Radiobutton(f_2, text='М', value='м', variable=gender)
    rad2 = Radiobutton(f_2, text='Ж', value='ж', variable=gender)
    label_2.pack(side=LEFT, padx=6)
    rad1.pack(side=LEFT)
    rad2.pack(side=LEFT)

    label_3 = Label(f_3, text="деятельность в течение дня", bg="AliceBlue", fg="CornflowerBlue", font=40)
    activiti_entry = Combobox(f_3, textvariable=activity, width=48, values=["прогулка", "ежедневные дела", "спорт"])
    label_3.pack()
    activiti_entry.pack()

    label_4 = Label(f_4, text="", bg="AliceBlue", font=40)
    label_4.pack()

    last_button = Button(window_second, text="НАЗАД", bg="pink", fg="HotPink4",
                         command=partial(open_first, window_second), width=15,
                         height=1)
    next_button = Button(window_second, text="ПРОДОЛЖИТЬ", bg="pink", fg="HotPink4",
                         command=partial(open_third, window_second),
                         width=15, height=1)

    # упорядочивание элементов окна
    f_0.pack(expand=1)
    f_1.pack(expand=1)
    f_2.pack(expand=1)
    f_3.pack(expand=1)
    f_4.pack(expand=1)

    last_button.pack(anchor=W)
    next_button.pack(anchor=E)

    last_button.pack(side=LEFT)
    next_button.pack(side=RIGHT)

    window_second.mainloop()

    return

'''
Третье окно интерфейса, итоги программы, вывод даты, города и соответствующих рекомендаций по одежде 
'''

def third_window():
    global recom
    global num
    global all_path
    num = 0

    try:
        get_weather(city.get(), parse(date.get()).strftime('%Y-%d-%m'))
    except:
        messagebox.showerror('ОШИБКА', 'Дата введена неверно, прогноз на только на 7 дней!')
        second_window()
        return
    
    def open_img(collection):
        x = openfilename(collection)
        img = Image.open(x)
        img = img.resize((250, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(window_third, image=img)
        panel.image = img
        panel.grid(row=4)

    def openfilename(collection):
        global num
        if num == len(collection):
            num = 0
            path = collection[num]
            num = num + 1
            return path
        else:
            path = collection[num]
            num = num + 1
            return path

    def get_all_path():
        os.chdir("autfits")
        path = os.getcwd()
        collection = []

        for dirs, folder, files in os.walk(path):
            if files != []:
                collection.append(os.path.join(str(dirs), str(files[0])))

        os.chdir("..")
        return collection

    all_path = get_all_path()

    # создание окна
    window_third = Tk()
    window_third.title('WEATHER_RESULT')
    window_third.geometry("750x450")
    window_third['bg'] = "AliceBlue"

    recom = StringVar()
    recom.set(main(city.get(), date.get(), gender.get(), activity.get()))  # вызов функции с кодом

    # ввод данных
    Label(text=f'{parse(date.get()).strftime("%d.%m.%y").lower()} | {(city.get()).upper()}', bg="AliceBlue", fg="CornflowerBlue", font='Helvetica 18 bold').grid(row=1)
    Label(text=recom.get(), bg="AliceBlue", fg="CornflowerBlue", font='Helvetica 12').grid(row=2)
    Button(text='изображение', command=partial(open_img, all_path), bg="Pink", fg="HotPink4").grid(row=3)
    Button(window_third, text="НАЗАД", bg="pink", fg="HotPink4", command=partial(open_second, window_third)).grid(row=5, sticky=SW)
    Button(window_third, text="ЗАКРЫТЬ", bg="pink", fg="HotPink4", command=partial(closed, window_third)).grid(row=5, sticky=SE)

    window_third.mainloop()


def main(user_city, user_date, user_gender, user_activity):
    global info_weather  # в переменной хранится вызов функции, переменнная глобальная для того чтобы вызывать функцую только один раз

    city_name, info_weather = get_weather(user_city, parse(user_date).strftime('%Y-%d-%m'))

    #city_name = 'спб'
    #info_weather = {'app_max_temp': -15.9, 'app_min_temp': -19.3, 'clouds': 42, 'clouds_hi': 20, 'clouds_low': 8,
    #                'clouds_mid': 37, 'datetime': '2023-01-08', 'dewpt': -17, 'high_temp': -12.3, 'low_temp': -13.6,
    #                'max_dhi': None, 'max_temp': -12.3, 'min_temp': -15.3, 'moon_phase': 0.947291,
    #                'moon_phase_lunation': 0.56, 'moonrise_ts': 1673186918, 'moonset_ts': 1673167742, 'ozone': 298.1,
    #                'pop': 0, 'precip': 0, 'pres': 1030.2, 'rh': 79, 'slp': 1032.2, 'snow': 0, 'snow_depth': 117.8,
    #                'sunrise_ts': 1673160988, 'sunset_ts': 1673183934, 'temp': -14, 'ts': 1673125260, 'uv': 1.5,
    #                'valid_date': '2023-01-08', 'vis': 24.128,
    #                'weather': {'description': 'Облачно с прояснениями', 'code': 803, 'icon': 'c03d'},
    #                'wind_cdir': 'ЮВ', 'wind_cdir_full': 'Юго-Восточный', 'wind_dir': 127, 'wind_gust_spd': 4,
    #                'wind_spd': 1.6}

    weather = f'средняя температура {round(info_weather["temp"])} C | скорость ветра {round(info_weather["wind_spd"])} м/с | {info_weather["weather"]["description"].lower()}'
    recomendation_clouses = f'рекомендуем надеть {get_clouses(user_city, user_date, user_gender, user_activity)[0][0]}'
    other_recomendation_clouses = f'{", ".join(recomendation(user_date, user_city)).lower()}'

    image(user_city, user_date, user_gender, user_activity)  # получаем изображения в папку

    return (f'\n {weather}'
            f'\n {recomendation_clouses}'
            f'\n {other_recomendation_clouses}')


# функция для получения информации с сайта погоды, исходя из данных пользователя, возвращает название города и сведения о погоде
def get_weather(user_city, user_date):
    print(user_city, user_date)
    print(type(user_city), type(user_date))
    # с сайта получаем прогноз погоды на 7 дней в введенном городе в формате json, только RU города
    r = requests.get(
        f'https://api.weatherbit.io/v2.0/forecast/daily?city={user_city},RU&key=3a37beb19b3b4d8981d9e4911cd60f77&lang=ru&days=7').json()

    info = {}  # из 7 дней выбираем тот, который нужен пользователю
    for item in r["data"]:
        if str(item['datetime']) == user_date:
            info = item

    return [r["city_name"], info]


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

    if info_weather['uv'] > 4 and info_weather['uv'] < 8:
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
    print(info_weather)
    print(user_gender, user_activity)
    print(type(user_gender), type(user_activity))
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
    print(recomendation_clouses)
    return recomendation_clouses


# функция для получения картинок по запросу
def image(user_city, user_date, user_gender, user_activity):
    # получение рекоммендации об одежде
    clouses = get_clouses(user_city, user_date, user_gender, user_activity)

    os.chdir("autfits")  # изменение текущего каталога на outfits

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

        os.chdir("..")  # возврвщаемся в outfits

    os.chdir("..")
    return

# старт программы с вызова первого окна
first_window()
