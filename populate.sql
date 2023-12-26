-- Вставка даних в таблицю MoviesAndShows
INSERT INTO MoviesAndShows (MovieOrShowID, Title, Type, ReleaseYear)
VALUES
    (1, 'Look Both Ways', 'Films', NULL),
    (2, 'Day Shift', 'Films', NULL),
    (3, 'Bank Robbers: The Last Great Heist', 'Films', NULL),
    (4, 'The Next 365 Days', 'Films', NULL),
    (5, 'The Angry Birds Movie 2', 'Films', NULL),
    (6, 'Purple Hearts', 'Films', NULL),
    (7, 'River Runs Red', 'Films', NULL),
    (8, '1917', 'Films', NULL),
    (9, 'Code Name: Emperor', 'Films', NULL);

-- Вставка даних в таблицю Weeks
INSERT INTO Weeks (WeekID, WeekStartDate, WeekEndDate)
VALUES
    (1, '2022-08-21', '2022-08-21');

-- Вставка даних в таблицю Countries
INSERT INTO Countries (CountryID, CountryName)
VALUES
    (1, 'Argentina');

-- Вставка даних в таблицю Ratings
INSERT INTO Ratings (RatingID, MovieOrShowID, WeekID, CountryID, Rank, Viewership, Duration)
VALUES
    (1, 1, 1, 1, 1, NULL, NULL),
    (2, 2, 1, 1, 2, NULL, NULL),
    (3, 3, 1, 1, 2, NULL, NULL),
    (4, 4, 1, 1, 1, NULL, NULL),
    (5, 5, 1, 1, 1, NULL, NULL),
    (6, 6, 1, 1, 4, NULL, NULL),
    (7, 7, 1, 1, 1, NULL, NULL),
    (8, 8, 1, 1, 2, NULL, NULL),
    (9, 9, 1, 1, 2, NULL, NULL);

-- Вставка даних в таблицю Ratings (глобальні)
INSERT INTO Ratings (RatingID, MovieOrShowID, WeekID, CountryID, Rank, Viewership, Duration)
VALUES
    (10, 1, 1, NULL, 1, 63390000, 2),
    (11, 2, 1, NULL, 2, 48060000, 1),
    (12, 4, 1, NULL, 1, 39310000, 1),
    (13, 6, 1, NULL, 4, 23410000, 4),
    (14, 5, 1, NULL, 1, 20050000, 1),
    (15, 9, 1, NULL, 2, 11470000, 1),
    (16, 8, 1, NULL, 3, 8660000, 3);
