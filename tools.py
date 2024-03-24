import json
import traceback

import psycopg2


class SQLTools:

    def __init__(self, data_base_url):
        self.cursor = None
        self.connect = None
        self.is_ok = False
        self.office_name = None
        self.employers_names = []
        self.data_to_seed = None
        self.data_base_url = data_base_url

    def connected(self):
        try:
            self.connect = psycopg2.connect(self.data_base_url)
            self.cursor = self.connect.cursor()
            self.is_ok = True

        except psycopg2.OperationalError:
            print("_-_-_Сообщение из SQLTools_-_-_")
            print('ОШИБКА ПОДКЛЮЧЕНИЯ \n',
                  traceback.format_exc(),
                  'Проверьте работоспособность базы и повторите попытку \n')

    def connection_close(self):
        self.connect.close()
        self.is_ok = False

    def json_loader(self, file):
        """
        Принимает местоположение файла, считывает его и возвращает
        Если файл не найден, возвращает None блокируя дальнейшие шаги
        :param file:
        :return:
        """
        try:
            with open(file, 'r') as jf:
                self.data_to_seed = json.load(jf)
                print("_-_-_Сообщение из SQLTools_-_-_")
            print(f"Были считаны следующие данные - {self.data_to_seed} \n")
        except FileNotFoundError:
            print("_-_-_Сообщение из SQLTools_-_-_")
            print("Файла не существует \n")

    def table_creator(self):
        try:
            create_table_query = """CREATE TABLE subordination
                                      (ID INT   PRIMARY KEY     NOT NULL,
                                      ParentId  INTEGER,
                                      Name      TEXT,
                                      Type      INTEGER); """
            # Выполнение команды: это создает новую таблицу
            self.cursor.execute(create_table_query)
            self.connect.commit()
            print("_-_-_Сообщение из SQLTools_-_-_")
            print("Таблица успешно создана в PostgreSQL \n")
        except psycopg2.errors.DuplicateTable:
            self.connect.commit()
            print("_-_-_Сообщение из SQLTools_-_-_")
            print('Ошибка: Таблица уже существует \n')

    def table_seeder(self):
        print("_-_-_Сообщение из SQLTools_-_-_")
        for data in self.data_to_seed:
            try:
                row_id = data['id']
                row_parent_id = data['ParentId']
                row_name = data['Name']
                row_type = data['Type']

                inserting = "INSERT INTO subordination(Id, ParentId, Name, Type) VALUES (%s, %s, %s, %s);"
                self.cursor.execute(inserting, (row_id, row_parent_id, row_name, row_type))
                self.connect.commit()
            except psycopg2.errors.UniqueViolation:
                print(f'Запись с ID - {row_id} уже существует')
                self.connect.commit()
            except KeyError:
                print(f'В записи {data} присутствуют ошибки')  # возможно стоит валидировать данные ранее?
                continue

    def search(self, employer_id):
        selecting_office = """WITH RECURSIVE r1 AS (
                       SELECT 
                         id, 
                         parentid, 
                         name, 
                         type 
                       FROM 
                         subordination 
                       WHERE 
                         id = %s -- сюда прилетает айди сотрудника 
                       UNION 
                       SELECT 
                         subordination.id, 
                         subordination.parentid, 
                         subordination.name, 
                         subordination.type 
                       FROM 
                         subordination 
                         JOIN r1 ON subordination.id = r1.parentid
                       ) 
                       SELECT id, name 
                       FROM r1 
                       WHERE 
                       type = 1;"""
        self.cursor.execute(selecting_office, (employer_id,))  # получаем данные офиса
        data = self.cursor.fetchone()
        office_id = data[0]
        self.office_name = data[1]
        print(office_id)
        selecting_employees = """
                                 WITH RECURSIVE r2 AS (
                                 SELECT 
                                    id, 
                                    parentid, 
                                    name, 
                                    type 
                                 FROM subordination 
                                 WHERE 
                                    parentid = %s 
                                 UNION 
                                 SELECT 
                                    subordination.id, 
                                    subordination.parentid, 
                                    subordination.name, 
                                    subordination.type 
                                 FROM subordination 
                                 JOIN r2 
                                 ON subordination.parentid = r2.id
                                 ) 
                                 SELECT name 
                                 FROM r2
                                 WHERE type=3;"""
        self.cursor.execute(selecting_employees, (office_id,))  # получаем сотрудников
        data = self.cursor.fetchall()
        for name in data:
            self.employers_names.append(name[0])
        print("_-_-_Сообщение из SQLTools_-_-_")
        print(f"Офис - {self.office_name},"
              f"Сотрудники - {self.employers_names}")
