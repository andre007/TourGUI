import sqlite3
# Create the database, a connection to it and a cursor
connection = sqlite3.connect('Touristdb.db')
cursor = connection.cursor()
# Execute the SQLite statement to create the Tourist table
cursor.execute("""
CREATE TABLE Tourist (TouristID integer primary key autoincrement, FirstName varchar (30) NOT NULL,  SecondName varchar(30) NOT NULL , ThirdName varchar(30), DateOfBirth date NOT NULL , CityOfBirth varchar (40) NOT NULL , CountryOfBirth varchar(30) NOT NULL , CitizenPassport varchar(30) NOT NULL , ForeignPassport varchar(30) NOT NULL , DateOfPasStart date NOT NULL , DateOfPasFin date NOT NULL , INN int(30) NOT NULL , Countries varchar(70) NOT NULL , HomeAdress varchar(70) NOT NULL , phone int(30) NOT NULL, Notes text )""") 


cursor.execute("INSERT INTO Tourist VALUES (null, 'Alexey', 'Griboyedov', 'Romanovich', '2013-11-11','Russia', 'Moscow', 'KM8551', 'IM458655', '2013-11-11', '2013-12-12', '1112324562', 'Germany', 'Moscow', '51561841', 'none')")

connection.commit()
cursor.close()
connection.close() 