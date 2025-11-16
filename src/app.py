import sqlite3
import pandas as pd

con = sqlite3.connect("Test.DB")

con.execute("CREATE TABLE movies(id INT PRIMARY KEY NOT NULL, title TEXT NOT NULL, year INT NOT NULL)")

con.execute("INSERT INTO movies VALUES (1, 'Titanic', 1997)")
con.execute("INSERT INTO movies VALUES (2, 'The Godfather', 1972)")
con.execute("INSERT INTO movies VALUES (3, 'Gladiator 2', 2025)")
con.commit()

cursor = con.execute("SELECT * FROM movies WHERE year > 1990")

for row in cursor:
  print(f'Title:{row[1]}, Year:{row[2]}')

con.close()