# Техническое задание Филиппов Н.Р.
Консольное приложение по работе с PostgreSQL, есть функции подключения к БД, заполнению данных из json файла и выборке сотрудников из того что офиса что и известный.



## Использование
Перед началом работы убедитесь что вы используете в качестве БД PostgreSQL 9.6 / 10:

Установите зависимости с помощью команды:
```sh
pip install -r requirements.txt
```
Добавьте свой файл .env в корень проекта и добавьте туда запись в формате
```sh
DATA_BASE_URL='postgresql://postgres:password@localhost:5433/tensor_tech_base'
```

Запустите файл main и последовательно проходите пункты меню
Подключитесь к базе данных
Создайте таблицу 
Введите название json файла (в проекте уже присутсвует data.json) 
Заполните таблицу данными
Введите айди известного сотрудника (так же можно ввести айди отдела)
Готово!






### Требования
Для установки и запуска проекта, необходим Python 3.10 или выше.


