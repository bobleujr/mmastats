import psycopg2

# def case1(request):
#

conn = psycopg2.connect(dbname="mmastats", user="common", password="011092", port="5432", host="localhost")
cur = conn.cursor()

cur.execute("SELECT get_fighter_basics(%s, %s)",('Edson Barboza', 'mycursor'))

cur.fetchone()

#cur.fetchone()
#ur.fetchall()
