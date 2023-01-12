# Прогноз одежды
## О программе ##

Мы разработали программу, которая:
* Подскажет Вам погоду на определенный день в вашем городе
* Даст рекомендации в выборе одежды, исходя из информации о Вас
* Посоветует взять с собой зонт\резиновые сапоги\солнечные очки и др.

Для того чтобы начать работу с программой:
1. скайчайте все файлы из папки MAIN в одну директорию
2. установите перечисленные ниже модули
3. запустите код (расширение .py)
>[MAIN](https://github.com/NataTyugun/project-3-semester/blob/main/final_job/LAST.py)

## Работа программы ##

Для рекомендации одежды нам потребуется следующая информация от пользователя:
* День, на который необходимо сделать прогноз (В улучшенной выбрать утро\день\вечер)
* Город, в котором необходимо сделать прогноз
* Пол пользователя, для более точной подборки
* Выбор вида активности на день (спорт\прогулка на улице\повседневные дела)


![ридми](https://user-images.githubusercontent.com/99788525/212077531-10ed9f52-31b1-44ae-8c42-7a66173a559a.png)



Пользователь получит информации в следующем формате:
* Погода на необходиму дату (температура\ветер\состояние)
* Рекомендация по подбору одежды (в зависимости от информации о пользователе)
* Рекомендация на случай сильного дождя\солнца\снега\ветра

![image](https://user-images.githubusercontent.com/99788525/212083315-6bdc5144-1f60-4980-983f-b54ff505a3c0.png)

## Реализация программы ##
1. Данные о погоде получены с сайта https://www.weatherbit.io/
2. База данных создана на основе данных погоды и информации от пользователей. Рекоммендации по одежде были составлены самостоятельно.
3. Особые рекомендации на случай сильно дождя\солнца\снега\ветра исходя из данных о погоде.
4. Интерфейс из 3 окон при помощи модуля tkinter.
5. Получение картинок одежды на основе рекоммендации при помощи модуля GoogleImageCrawler.
6. Для удобного использования программы прописаны ошибки.

![image](https://user-images.githubusercontent.com/99526918/212069023-6a4db738-03ea-4e38-a1c4-5a2b01dd4196.png)

***
Работу выполнили: Воробьева Анастасия, Тюгун Наталья
