import psycopg2


def create_tables():
    tables = [
        """
        CREATE TABLE Orders (
            id VARCHAR(64) PRIMARY KEY,
            price FLOAT NOT NULL,
            amount FLOAT NOT NULL,
            order_type VARCHAR(64) NOT NULL
        )
        """
    ]
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(dbname='trade_bot', user='postgres',
                        password='postgres', host='localhost', port=5439)
        cur = conn.cursor()
        # create table one by one
        for command in tables:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
