import psycopg2
import numpy as np
import matplotlib.pyplot as plt


username = 'postgres'
password = 'postgres'
database = 'lab_3_6'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT R.Rank, AVG(R.Duration) AS AverageDuration
FROM Ratings R
GROUP BY R.Rank;
'''
query_2 = '''
SELECT R.CountryID, COUNT(*) AS Count
FROM Ratings R
GROUP BY R.CountryID
ORDER BY Count DESC
LIMIT 5;
'''
query_3 = '''
SELECT M.ReleaseYear, AVG(R.Rank) AS AverageRank
FROM MoviesAndShows M
JOIN Ratings R ON M.MovieOrShowID = R.MovieOrShowID
GROUP BY M.ReleaseYear
ORDER BY M.ReleaseYear;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    # Task 1
    cur.execute(query_1)
    ranks = []
    durations = []

    for row in cur:
        ranks.append(row[0])
        durations.append(row[1])

    fig, ax = plt.subplots(1, 3)
    ax[0].bar(ranks, durations, color='g', edgecolor='y')
    ax[0].set_title('Average Duration by Rank')
    ax[0].set_xlabel('Rank')
    ax[0].set_ylabel('Average Duration')

    # Task 2
    cur.execute(query_2)
    country_ids = []
    counts = []

    for row in cur:
        country_ids.append(row[0])
        counts.append(row[1])

    ax[1].pie(counts, labels=country_ids, autopct='%1.1f%%', 
              wedgeprops={'edgecolor':'y'})
    ax[1].set_title('Top 5 Countries by Rating Count')

    # Task 3
    cur.execute(query_3)
    release_years = []
    average_ranks = []

    for row in cur:
        release_years.append(row[0])
        average_ranks.append(row[1])

    ax[2].plot(release_years, average_ranks, color='g', marker='o')
    ax[2].set_title('Average Rank by Release Year')
    ax[2].set_xlabel('Release Year')
    ax[2].set_ylabel('Average Rank')

mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()
