#Created by Nicholas Caballero
import mysql.connector
import CRUD
import prettytable
from prettytable import from_db_cursor
import datetime

CaballeroAirportSupply=mysql.connector.connect(host="127.0.0.1", user="ncaballero", password="LetMeIn420$", db="lab3and4")

cursor=CaballeroAirportSupply.cursor()
print("Created by Nicholas Caballero\n")
username=input("Enter your username: \n")
password=input("Enter your password: \n")

usernameQuery="select * from user_and_password WHERE user = '" + username + "'"
cursor.execute(usernameQuery)
queryNameResult=cursor.fetchall()

# print("\nUsername: "+str(queryNameResult[0][0])+"\nPassword: "+str(queryNameResult[0][1]))
# print("\nInputU: "+username+"\nInputP: "+password)


while (username!=str(queryNameResult[0][0]) or password!=str(queryNameResult[0][1])):
        print("Error: Wrong username and password\n")
        username=input("Enter your username: \n")
        password=input("Enter your password: \n")

# username!=str(queryNameResult[0][0])) and password!=str(queryNameResult[1]

print("Successful Login")
print("\nCreated by Nicholas Caballero\n")

commandInput=""

while(commandInput!="Exit"):
    commandInput=input("\nPlease enter in a command \n" +
    "Enter \"C\" to Create new data \n" +
    "Enter \"R\" to Read from the database \n" +
    "Enter \"U\" to Update currently existing data \n" +
    "Enter \"D\" to Delete data \n"+
    "Enter \"Exit\" to terminate the program\nCommand: ")
    CRUD.CRUD(commandInput,cursor,CaballeroAirportSupply,username)

print("\nTermination successful")
print("\nCreated by Nicholas Caballero\n")