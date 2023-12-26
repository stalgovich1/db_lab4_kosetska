-- Таблиця фільмів/шоу
CREATE TABLE MoviesAndShows (
    MovieOrShowID INT PRIMARY KEY,
    Title VARCHAR(255),
    Type VARCHAR(50),
    ReleaseYear INT
);

-- Таблиця тижнів
CREATE TABLE Weeks (
    WeekID INT PRIMARY KEY,
    WeekStartDate DATE,
    WeekEndDate DATE
);

-- Таблиця країн
CREATE TABLE Countries (
    CountryID INT PRIMARY KEY,
    CountryName VARCHAR(100)
);

-- Таблиця рейтингів
CREATE TABLE Ratings (
    RatingID INT PRIMARY KEY,
    MovieOrShowID INT,
    WeekID INT,
    CountryID INT,
    Rank INT,
    Viewership INT,
    Duration INT,
    FOREIGN KEY (MovieOrShowID) REFERENCES MoviesAndShows(MovieOrShowID),
    FOREIGN KEY (WeekID) REFERENCES Weeks(WeekID),
    FOREIGN KEY (CountryID) REFERENCES Countries(CountryID)
);
