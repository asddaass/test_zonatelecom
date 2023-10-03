# Работоспособность не проверял(скорее всего не работает), добавил просто для примера как это может выглядеть,

from mysql.connector import Error, connect
import config


class MySQLClient:

    @staticmethod
    def __connection():
        try:
            connection = connect(host=config.db_host, user=config.db_user, password=config.db_pass)
            return connection

        except Error as e:
            print(e)

    @staticmethod
    def __close(conn, cursor):
        cursor.close()
        conn.close()

    def select(self, query):
        conn = self.__connection()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        self.__close(conn, cursor)
        return rows