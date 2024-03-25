from settings import DATA_BASE_URL
from tools import SQLTools


def intetface():
    """
    Консольный интерфейс
    В зависимости от надобности в блок со статусом подключения можно добавить еще пунктов
    Большинство пунктов смогут отработать только после подключения к базе и предыдущего пункта
    :return:
    """
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
            if base.data_to_seed:  # отрабатывает только если есть подготовленные данные
                base.table_seeder()
            else:
                print(">>>Данные для таблицы не подготовлены<<<")
        elif user_choice == '5':
            if base.is_ok:
                user_choice = input("Введите id сотрудника \n"
                                    "---> ")
                try:
                    base.search(int(user_choice))
                except TypeError:  # если было введено не число не допускает запуск выборки
                    print("Ошибка ввода id \n")
            else:
                print("Вы не подключены к базе \n")

        elif user_choice == '6':
            if base.is_ok:
                base.connection_close()
            else:
                print("Вы не подключены к базе \n")
        elif user_choice == '7':
            print("До свидания! ")
            base.connection_close()
            break
        else:
            print("Команда не распознана, попробуйте снова \n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    intetface()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
