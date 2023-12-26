import psycopg2
import numpy as np
import matplotlib.pyplot as plt

# Параметри підключення до бази даних
connection_params = {
    'user': 'postgres',
    'password': 'postgres',
    'dbname': 'lab_3_6',
    'host': 'localhost',
    'port': '5432'
}

# SQL-запити
query_1 = '''
SELECT ReleaseYear, AVG(Duration) AS AvgDuration
FROM Ratings
JOIN MoviesAndShows ON Ratings.MovieOrShowID = MoviesAndShows.MovieOrShowID
GROUP BY ReleaseYear
ORDER BY ReleaseYear;
'''

query_2 = '''
SELECT CountryName, SUM(Viewership) AS TotalViewership
FROM Ratings
JOIN Countries ON Ratings.CountryID = Countries.CountryID
GROUP BY CountryName
ORDER BY TotalViewership DESC;
'''

query_3 = '''
SELECT Type, AVG(Duration) AS AvgDuration
FROM Ratings
JOIN MoviesAndShows ON Ratings.MovieOrShowID = MoviesAndShows.MovieOrShowID
GROUP BY Type;
'''

# Встановлення з'єднання з базою даних
with psycopg2.connect(**connection_params) as conn:
    with conn.cursor() as cur:
        # Виконання запитів та отримання результатів
        cur.execute(query_1)
        years_1, durations_1 = zip(*cur.fetchall())

        cur.execute(query_2)
        countries, total_viewership = zip(*cur.fetchall())

        cur.execute(query_3)
        types, avg_durations = zip(*cur.fetchall())

# Побудова візуалізацій
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Task 1
ax[0].bar(years_1, durations_1, color='g', edgecolor='y')
ax[0].set_title('Середня тривалість фільмів/шоу за роками')
ax[0].set_xlabel('Рік')
ax[0].set_ylabel('Середня тривалість')

# Task 2
ax[1].pie(total_viewership, labels=countries, autopct='%1.1f%%', wedgeprops={'edgecolor': 'y'})
ax[1].set_title('Загальна кількість переглядів за країною')

# Task 3
ax[2].scatter(types, avg_durations, color='g')
ax[2].set_title('Середня тривалість фільмів/шоу за типом')
ax[2].set_xlabel('Тип')
ax[2].set_ylabel('Середня тривалість')

plt.show()
