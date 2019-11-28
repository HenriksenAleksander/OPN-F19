create database person;
use person;

CREATE TABLE persons (
  PersonID int AUTO_INCREMENT PRIMARY KEY,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL
);
