import sqlite3
# Create a connection to the database and a cursor
connection = sqlite3.connect('Touristdb.db')
cursor = connection.cursor()
# Add a CD to the database
NameVal = raw_input("Name ")
SecoNdnameVal = raw_input("Second name? ")
ThirdNameVal = raw_input("Third Name? ")
DateOfBirthVal = raw_input("Date of Birth? ")
CityOfBirthVal = raw_input("City of birth? ")
CountryOfBirthVal = raw_input("Country of birth? ")
CitizenPassportVal = raw_input("Citizen Passport? ")
ForeignPassportVal = raw_input("Foreign Passport? ")
DateOfPasStartVal = raw_input("Date of foreign passport start? ")
DateOfPasFinVal = raw_input("Date of foreign passport fin? ")
INNVal = raw_input("INN? ")
CountriesVal = raw_input("Countries to visit? ")
HomeAdresVal = raw_input("Home adress? ")
PhoneVal = raw_input("Phone ? ")
NotesVal = raw_input("Notes? ")

cursor.execute("INSERT INTO Tourist VALUES (null, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (NameVal, SecoNdnameVal, ThirdNameVal, DateOfBirthVal, CityOfBirthVal, CountryOfBirthVal, CitizenPassportVal, ForeignPassportVal, DateOfPasStartVal, DateOfPasFinVal, INNVal, CountriesVal, HomeAdresVal, PhoneVal, NotesVal))
# Commit the transaction and close the connection
connection.commit()
cursor.close()
connection.close()