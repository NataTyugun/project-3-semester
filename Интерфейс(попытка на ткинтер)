# import sqlite3
from tkinter import *
# from tkinter import ttk
from tkinter.ttk import Radiobutton
from functools import partial
# from tkinter import messagebox

"""
Закрывает текущее окно, открывает окно с приемом пищи
"""


def closed(win):
    win.destroy()


def open_first(win_close):
    win_close.destroy()
    first_window()


def open_second(win_close):
    win_close.destroy()
    second_window()


def open_third(win_close):
    win_close.destroy()
    third_window()


def sport():
    user_activity = 'спорт'
    return user_activity


def walk():
    user_activity = 'прогулка'
    return user_activity


def work():
    user_activity = 'ежедневные дела'
    return user_activity


def info(user_date, user_city):
    user_info = user_date + '  ' + user_city
    return user_info


"""
Окно для рассчета дневной нормы ккал пользователя (запускается первым при старте программы)
"""


def first_window():
    # интерфейс окна для рассчета дневной нормы ккал
    window_first = Tk()
    window_first.title('WEATHER_CITY')
    window_first.geometry("300x300")
    window_first['bg'] = 'lavender'
    # photo = PhotoImage(file='C:\Users\User\Desktop\natalie\oblaco_big.png')
    # window_first.iconphoto(False)
    canvas = Canvas(window_first, width = 80, height = 60, bg = 'lavender')


    oblaco = PhotoImage(file='oblaco.png')
    canvas.create_image(20,20,anchor = NW, image = oblaco)

    # переменные для ввода данных
    user_city = StringVar()

    # блок невидимых рамок для красивого интерфейса
    f_0 = Frame(window_first)
    f_1 = Frame(window_first)
    f_2 = Frame(window_first)
    f_3 = Frame(window_first)
    # ввод данных

    label = Label(f_0, text="ПРОГНОЗ ОДЕЖДЫ", bg="lavender", fg='midnightblue', font=('Arial 20 underline'), width=30,
                  height=1)

    label_1 = Label(f_1, text="ВВЕДИТЕ ВАШ ГОРОД", bg="lavender", fg='midnightblue', font=70, width=30, height=1)

    city_entry = Entry(f_2, width=70, textvariable=user_city)

    close_button = Button(window_first, text="ЗАКРЫТЬ", bg="pink", command=partial(closed, window_first),  width=15, height=1)

    next_button = Button(window_first, text="ПРОДОЛЖИТЬ", bg="pink", command=partial(open_second, window_first),  width=15, height=1)

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

    return user_city


def second_window():
    # интерфейс окна для рассчета дневной нормы ккал
    window_second = Tk()
    window_second.title('WEATHER_RESULT')
    window_second.geometry("500x400")
    window_second['bg'] = 'lavender'
    # photo = PhotoImage(file='oblaco.png')
    # window_second.iconphoto(False)

    # переменные для ввода данных
    user_date = StringVar()
    user_gender = StringVar()
    user_activity = StringVar()

    # блок невидимых рамок для красивого интерфейса
    f_0 = Frame(window_second)
    f_1 = Frame(window_second)
    f_2 = Frame(window_second)
    f_3 = Frame(window_second)
    f_4 = Frame(window_second, bg= 'lavender')
    f_5 = Frame(window_second)
    f_6 = Frame(window_second, bg= 'lavender')

    # ввод данных

    label = Label(f_0, text="ПОЛЬЗОВАТЕЛЬСКАЯ ИНФОРМАЦИЯ", bg="lavender", fg='midnightblue',
                  font=(' Arial 20 underline'), width=40, height=1)

    label_1 = Label(f_1, text="ДАТА", bg="lavender", fg='midnightblue', font=70, width=40, height=1)

    date_entry = Entry(f_2, width=8, textvariable=user_date)

    label_2 = Label(f_3, text="ПОЛ", bg="lavender", fg='midnightblue', font=70, width=30, height=1)

    rad1 = Radiobutton(f_4, text='М', value=4, variable=user_gender)

    rad2 = Radiobutton(f_4, text='Ж', value=-161, variable=user_gender)

    label_3 = Label(f_5, text="ДЕЯТЕЛЬНОСТЬ", bg="lavender", fg='midnightblue', font=70, width=30, height=1)

    walk_button = Button(f_6, text="прогулка", bg="pink", command=walk(), width=12, height=2)
    sport_button = Button(f_6, text="спорт ", bg="pink", command=sport(), width=12, height=2)
    work_button = Button(f_6, text="дела", bg="pink", command=work(), width=12, height=2)

    last_button = Button(window_second, text="НАЗАД", bg="pink", command=partial(open_first, window_second), width=15, height=1)
    next_button = Button(window_second, text="ПРОДОЛЖИТЬ", bg="pink", command=partial(open_third, window_second), width=15, height=1)

    # упорядочивание элементов окна
    f_0.pack(pady=5, expand=1)
    f_1.pack(pady=5, expand=1)
    f_2.pack(pady=5, expand=1)
    f_3.pack(pady=5, expand=1)
    f_4.pack(pady=5, expand=1)
    f_5.pack(pady=5, expand=1)
    f_6.pack(pady=5, expand=1)
    last_button.pack(anchor = W)
    next_button.pack(anchor = E)
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

    return user_date, user_gender, user_activity


user_info = 'fvfdjvnd'
recomendation='vnjdkfn vk'

def third_window():
    global user_info
    global recomendation
    # интерфейс окна для рассчета дневной нормы ккал
    window_third = Tk()
    window_third.title('WEATHER_INFO')
    window_third.geometry("500x500")
    window_third['bg'] = 'lavender'
    # photo = PhotoImage(file='oblaco.png')
    # window_second.iconphoto(False)

    label = Label(textvariable=user_info, bg="lavender", fg='midnightblue', font=90, width=30, height=1)

    # блок невидимых рамок для красивого интерфейса
    f_0 = Frame(window_third)
    f_1 = Frame(window_third)
    f_2 = Frame(window_third)
    f_3 = Frame(window_third)
    f_4 = Frame(window_third)
    f_5 = Frame(window_third)

    # ввод данных
    label_1 = Label(f_1, text="ПОГОДА", bg="lavender", fg='midnightblue', font=70, width=30, height=1)
    label_2 = Label(f_3, textvariable=recomendation, bg="lavender", fg='midnightblue', font=70, width=30, height=1)
    label_3 = Label(f_4, text="ПРИМЕР ОДЕЖДЫ", bg="lavender", fg='midnightblue', font=70, width=30, height=1)
    recomendation_entry = Entry(f_5, width=70)

    last_button = Button(window_third, text="НАЗАД", bg="pink", command=partial(open_second, window_third),width=15, height=1 )
    next_button = Button(window_third, text="ЗАКРЫТЬ", bg="pink", command=partial(closed, window_third),width=15, height=1)

    # упорядочивание элементов окна
    f_0.pack(pady=5)
    f_1.pack(pady=5)
    f_2.pack(pady=5)
    f_3.pack(pady=5)
    f_4.pack(pady=5)
    f_5.pack(pady=5)
    last_button.pack(anchor = SW)
    next_button.pack(anchor = SE)
    last_button.pack(side= LEFT)
    next_button.pack(side = RIGHT)

    label.pack(side=LEFT)
    label_1.pack(side=LEFT)
    label_2.pack(side=LEFT)
    label_3.pack(side=LEFT)
    recomendation_entry.pack(side=LEFT,expand=1 )

    window_third.mainloop()

    return


# старт программы с вызова первого окна
first_window()
