import psycopg2

# Create Table


def create_table():
    conn = psycopg2.connect("dbname=lol user=postgres")

    cur = conn.cursor()

    cur.execute("CREATE TABLE test (key integer PRIMARY KEY, name text, title text);")

    conn.commit()

    cur.close()
    conn.close()

    print('Create DB --> OK')


def insert_record(item=dict()):
    key = item['key']
    name = item['name'].replace("\'", "\'\'")   # doubling single quote
    title = item['title'].replace("\'", "\'\'") # doubling single quote

    query = (
        'INSERT INTO public.test(key, name, title) '
        'VALUES ({0}, \'{1}\', \'{2}\');'
    ).format(key, name, title)

    conn = psycopg2.connect('dbname=lol user=postgres')
    cur = conn.cursor()

    cur.execute(query)

    conn.commit()

    cur.close()
    conn.close()


def get_record(key=0):
    query = ( 'SELECT * FROM public.test WHERE key={0}' ).format(key)
    conn = psycopg2.connect('dbname=lol user=postgres')
    cur = conn.cursor()

    cur.execute(query)

    records = cur.fetchall()

    cur.close()
    conn.close()

    return {'key': records[0][0], 'name': records[0][1], 'title': records[0][2]}


if __name__ == '__main__':
    print(get_record(1))

