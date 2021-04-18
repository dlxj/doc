
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import sys

def readImage(fname):

    fin = None

    try:
        fin = open(fname, "rb")
        img = fin.read()
        return img

    except IOError as e:

        print(f'Error {e.args[0]}, {e.args[1]}')
        sys.exit(1)

    finally:

        if fin:
            fin.close()


if __name__ == "__main__":

    data = readImage("t.mp3")
    binary = psycopg2.Binary(data)

    host = '209.141.34.77'
    port = 54322

    '00:01:12.960'
    '00:01:14.640'

    with psycopg2.connect(database='postgres', user='postgres', password='postgres',host=host, port=port) as conn:
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO audio(data) VALUES(%s);""", (binary,))
    
    print('ok.')


