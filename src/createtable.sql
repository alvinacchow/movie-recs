CREATE DATABASE IF NOT EXISTS movierecs;
USE movierecs;


CREATE TABLE IF NOT EXISTS user (
    email VARCHAR(50) PRIMARY KEY,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    password VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS movie (
    movieID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    releaseYear INT,
    description TEXT
);

CREATE TABLE IF NOT EXISTS watch_history (
    watchID INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(50),
    movieID INT,
    watchDate DATETIME NOT NULL,
    FOREIGN KEY (email) REFERENCES user(email),
    FOREIGN KEY (movieID) REFERENCES movie(movieID)
);
