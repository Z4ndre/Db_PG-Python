import psycopg2
from messageBoxes import show_notification


class DataBase():
    def __init__(self):
        super().__init__()
        self.connect_to_Db()

    def connect_to_Db(self):
        try:
            self.conn = psycopg2.connect(
                dbname='restore_cinema_db',
                user='postgres',
                password='12345',
                host='localhost',
                port='5432'
            )
            return self.conn
        except psycopg2.Error as e:
            show_notification(f"EROR: {e}")

    def get_procedures(self, name_file='procedures_in_db.txt'):
        try:
            self.connect_to_Db()
            cur = self.conn.cursor()
            cur.execute(
                """
                SELECT routine_name
                FROM information_schema.routines
                WHERE routine_type = 'PROCEDURE'
                AND specific_schema NOT IN ('pg_catalog', 'information_schema');
                """
            )
            procedures = cur.fetchall()

            with open(name_file, 'w') as file:
                for procedure in procedures:
                    file.write(procedure[0] + '\n')

            show_notification("Процедуры записаны в файл")

        except psycopg2.Error as e:
            show_notification(f"ERROR: {e}")
        finally:
            if self.conn:
                self.conn.close()

    def get_functions(self, name_file='functions_in_db.txt'):
        try:
            self.connect_to_Db()
            cur = self.conn.cursor()
            cur.execute(
                """
                SELECT routine_name
                FROM information_schema.routines
                WHERE routine_type = 'FUNCTION'
                AND specific_schema NOT IN ('pg_catalog', 'information_schema');
                """
            )
            functions = cur.fetchall()

            with open(name_file, 'w') as file:
                for function in functions:
                    file.write(function[0] + '\n')

            show_notification("Функции записаны в файл")

        except psycopg2.Error as e:
            show_notification(f"ERROR: {e}")
        finally:
            if self.conn:
                self.conn.close()

    def get_tables(self, name_file='table_list.txt'):
        try:
            self.connect_to_Db()
            cur = self.conn.cursor()
            cur.execute(
                """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                """
            )
            name_tables = cur.fetchall()

            with open(name_file, 'w') as fi:
                for table in name_tables:
                    fi.write(table[0] + '\n')

            show_notification("Список таблиц записан в файл")

        except psycopg2.Error as e:
            show_notification(f"ERROR: {e}")
        finally:
            if self.conn:
                self.conn.close()

    '''
    def get_data_from_PostgreSQL(self, script):
        try:
            self.connect_to_Db()
            cur = self.conn.cursor()
            cur.execute(
                f"""
                    {script}
                    """
            )
            text_script = cur.fetchall()
            return text_script

        except psycopg2.Error as e:
            show_notification(f"ERROR: {e}")
        finally:
            if self.conn:
                self.conn.close()
    '''

