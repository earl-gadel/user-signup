import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = mysql.connector.connect(host='localhost',
                                       database='user-signup',
                                       user='user-signup',
                                       password='Welcome2signup')

    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='user-signup',
                                       user='user-signup',
                                       password='Welcome2signup')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()