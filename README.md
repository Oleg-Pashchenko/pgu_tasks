# Решения лаб ПГУ
<div align="center">
  <img src=logo.jpeg width=250 height=250>
</div>

## Задание №1 [[Решение](https://github.com/Oleg-Pashchenko/pgu_tasks/blob/main/task_1/)]
1. Написать программу, распаковывающую архив и делающую его копию, исключая из 
копирования файлы по заданной преподавателем маске. Решение оформить в виде 
функции, принимающей на вход четыре аргумента: имя архива, каталог для 
распаковывания, каталог для копирования и маску. Для всех аргументов, кроме имени 
архива, предусмотреть умолчания. 
2. Написать функцию, принимающую на входе один аргумент — имя каталога, и 
возвращающую кортеж из двух списков — список файлов данного каталога и список 
подкаталогов данного каталога. 
3. Написать функцию обхода дерева каталогов и печати его содержимого. На вход 
функции передается один параметр — имя каталога. При печати элементы каждого 
уровня вложения должны выводиться с отступом 4*n, где n — уровень вложения. 
Уровень 0 соответствует исходному каталогу (его тоже надо печатать). 
Примечание: для обхода дерева каталогов удобно использовать стек, помещая в него 
еще не обработанные каталоги, и обрабатывать, извлекая из стека очередной 
каталог. 
4. Написать функцию поиска всех файлов с заданным расширением в дереве каталогов. 
У функции должно быть два аргумента — имя каталога и искомое расширение файла. 
Функция должна возвращать список с абсолютными именами найденных файлов. 
Примечание: задание 3 и 4 должны выполняться с использованием различных 
библиотек, например задание 3 с использованием os и os.path, а задание 4 — с 
использованием pathlib (или наоборот;))

## Задание №2 [[Решение](https://github.com/Oleg-Pashchenko/pgu_tasks/blob/main/task_2/main.py)]
1. Разработайте класс Dice, моделирующий бросание игральных костей. Объект данного 
класса при инициализации должен получать информацию о числе граней игральных 
костей (по умолчанию 6) и количестве костей в броске (по умолчанию 1). Реализуйте 
у класса метод, который возвращает случайный результат броска в виде кортежа или 
списка. 
2. Модифицируйте класс Dice так, чтобы при указании определенного значения seed при 
инициализации различных объектов класса можно было получить одну и туже 
последовательность результатов. Например такой код: 
d1 = Dice(seed=999) 
d2 = Dice(seed=999) 
print(*d1.roll(), *d2.roll()) 
print(*d1.roll(), *d2.roll()) 
print(*d1.roll(), *d2.roll()) 
даст одинаковые значения для двух костей при каждом вызове: 
6 6
1 1 
5 5 
3. Используйте разработанный класс для проведения статистического эксперимента по 
вычислению частоты выпадения разных значений при бросании пары шестигранных 
костей. Выпавшее значение принимать равным сумме показаний на гранях костей (от 
2 до 12). Для получения статистики необходимо бросить кости не менее 100000 раз. 
4. Разработайте функцию генерации случайного имени файла заданной длины и с 
заданным расширением (суффиксом). Имя должно состоять только из букв 
английского алфавита в разных регистрах. Напишите программу, демонстрирующую 
работу этой функции. 
5. Разработайте класс Password для генерации паролей. Объект данного класса при 
инициализации должен получать информацию о наборах символов, обязательных к 
использованию в пароле (как минимум один символ из каждого набора). Реализуйте у 
класса метод, генерирующий пароль заданной длины. Длина пароля должна 
передаваться методу в качестве параметра. Пароль должен возвращаться в виде 
строки. Напишите программу для демонстрации работы класса и проверки 
корректности его работы.

## Задание №3 [[Решение](https://github.com/Oleg-Pashchenko/pgu_tasks/blob/main/task_3/main.py)]
1. Некоторые двоичные файлы имеют в начале специальную сигнатуру, позволяющую 
определить их тип. Вам дано несколько файлов без расширений. Необходимо написать 
программу, которая проанализирует сигнатуры файлов и переименует файлы, добавив 
к каждому имени суффикс в соответствии с его типом, определенным с помощью 
сигнатуры. Типы файлов и их сигнатуры приведены в таблице 3. 
2. Дано несколько текстовых файлов, созданных в ОС Windows. Напишите программу, 
определяющую кодировку каждого файла и выводящую на экран их содержимое, если 
известно, что каждый файл начинается с символов «Привет».

## Задание №4
1. Спроектируйте интерфейс командной строки для генератора паролей, предусмотрев в
нем следующие возможности:
• указание количества генерируемых паролей (1 и больше);
• указание длины генерируемых паролей (5 и больше);
• указание алфавита генерируемых паролей (использовать множества цифр, английских
строчных и английских прописных);
2. Реализуйте интерфейс командной строки для генератора паролей с использованием
модуля argparse. Выполните тестирование интерфейса.
3. Используя класс Password, разработанный в предыдущей лабораторной работе, и
интерфейс командной строки, реализованный в предыдущем пункте задания, создайте
приложение для генерации паролей с интерфейсом командной строки. Проведите
демонстрацию всех возможностей разработанного приложения.

## Задание №5
1. Создайте сервер, работающий по протоколу TCP, который запрашивает у клиента
фамилию. Если фамилия принадлежит студенту вашей группы, то сервер посылает
приветсвие вида «Привет, имя_студента», напрмер, «Привет, Наташа». Если такой
фамилии нет, то сервер отвечает сообщением об ошибке. Формат сообщения об
ошибке произвольный. Порт сервера выбрать самостоятельно. Для проверки работы
сервера использовать утилиту nc в формате nc localhost
server_port.
2. Измените программу п.1 так, чтобы сервер работал по протоколу UDP. Для проверки
используйте nc -u localhost
server_port.
3. Создайте программу-клиента для HTTPS протокола и загрузите страницу по адресу
«https://beda.pnzgu.ru/anatoly/»
4. Модифицируйте программу из п.3 так, чтобы она загружала и сохраняла в файлы все
рисунки с загруженной страницы
5. Модифицируйте программу из п.4 так, чтобы она переходила по всем ссылкам в
тексте исходной страницы и сохраняла в файлы все рисунки с загруженных страницы. 
