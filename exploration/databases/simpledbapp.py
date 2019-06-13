from configparser import ConfigParser
import psycopg2


def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def connect():
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database ... ')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()
        ps_query = "select * from account"

        print('Getting all account information...')
        cur.execute(ps_query)

        account_data = cur.fetchall()

        print("Printing all rows:")
        for row in account_data:
            print("User Name: " + row[1])
            print("Email: " + row[3])
            print("Date Created: " + row[4].strftime("%m-%d-%y %H:%M:%S"))
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print('Database Connection closed.')


if __name__ == '__main__':
    connect()
