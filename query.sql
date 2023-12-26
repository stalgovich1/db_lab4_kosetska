--Вибрати всі фільми
SELECT * FROM MoviesAndShows;

--Вибрати всі країни
SELECT * FROM Countries;

--Вибрати всі рейтинги разом із назвою фільму/шоу та ім'ям країни
SELECT MoviesAndShows.Title, Countries.CountryName, Ratings.Rank, Ratings.Viewership, Ratings.Duration
FROM Ratings
JOIN MoviesAndShows ON Ratings.MovieOrShowID = MoviesAndShows.MovieOrShowID
JOIN Countries ON Ratings.CountryID = Countries.CountryID;
