# This is a sample Python script.
import keyboard

from settings import DATA_BASE_URL
from tools import SQLTools


# Press R to execute it or replace it with your code.
# Press Double  to search everywhere for classes, files, tool windows, actions, and settings.

def sql_tools():
    print("Вас приветствует SQLTools")
    base = SQLTools(
        data_base_url=DATA_BASE_URL
    )

    while True:
        print("****************************\n"
              f"Статус подключения - {base.is_ok} \n"
              "****************************\n")

        user_choice = input("[1] Подключиться к базе \n"
                            "[2] - Создать таблицу \n"
                            "[3] - Считать данные из json файла \n"
                            "[4] - Заполнить таблицу заполненными данными \n"
                            "[5] - Найти сотрудников по id одного из них \n"
                            "[6] - Отключиться от базы \n"
                            "[7] - Завершить работу \n"
                            "---> "
                            )

        if user_choice == '1':
            if base.is_ok:
                print(">>>Вы уже подключены!<<< \n")
            else:
                base.connected()
        elif user_choice == '2':
            if base.is_ok:
                base.table_creator()
            else:
                print(">>>Вы еще не подключены<<< \n")
        elif user_choice == '3':
            user_choice = input("Введите название json файла \n"
                                "---> ")
            base.json_loader(user_choice)
        elif user_choice == '4':
            if base.data_to_seed:
                base.table_seeder()
            else:
                print(">>>Данные для таблицы не подготовлены<<<")
        elif user_choice == '5':
            if base.is_ok:
                user_choice = input("Введите id сотрудника \n"
                                    "---> ")
                try:
                    base.search(int(user_choice))
                except TypeError:
                    print("Ошибка ввода id")
            else:
                print("Вы не подключены к базе \n")

        elif user_choice == '6':
            if base.is_ok:
                base.connection_close()
            else:
                print("Вы не подключены к базе \n")
        elif user_choice == '7':
            print("До свидания! ")
            break
        else:
            print("Команда не распознана, попробуйте снова \n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sql_tools()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
