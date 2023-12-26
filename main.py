import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = '5432'
database = 'db_lab3'
host = 'localhost'
port = '5432'

query_1 = '''
-- Загальний рейтинг (weekly_rank) для фільму "Red Notice" за всі країни
SELECT ac.show_title, ac.country_name, ag.weekly_rank FROM  all_weeks_countries ac
JOIN all_weeks_global ag ON ac.show_title = ag.show_title
WHERE ac.show_title = 'Red Notice'
UNION ALL

'''
query_2 = '''
-- Кількість годин перегляду для кожного фільму в Аргентині
SELECT ac.show_title, ac.country_name, mp.hours_viewed_first_28_days
FROM  all_weeks_countries ac
JOIN most_popular mp ON ac.show_title = mp.show_title
WHERE ac.country_name = 'Argentina'
UNION ALL
'''
query_3 = '''
-- Загальний рейтинг (weekly_rank) для фільму за всі країни
SELECT ac.show_title, ac.country_name
FROM all_weeks_countries ac
JOIN all_weeks_global ag ON ac.show_title = ag.show_title;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
                       
    cur = conn.cursor()

    print('Загальний рейтинг (weekly_rank) для фільму "Red Notice" за всі країни:')
    cur.execute(query_1)

    for row in cur:
       print(row)

    print('\nКількість годин перегляду для кожного фільму в Аргентині:')
    cur.execute(query_2)

    for row in cur:
       print(row)

    print('\nЗагальний рейтинг (weekly_rank) для фільму за всі країни:')
    cur.execute(query_3)

    for row in cur:
       print(row)