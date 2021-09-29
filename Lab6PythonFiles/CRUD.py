#Created by Nicholas Caballero
import Create
import Update
import Read
import Delete

def CRUD(userInput,databaseCursor,database,username):
    if(userInput=="C"):
        createInput=input("\nPlease select what type of data you would like to create\n"+
        "Type \"L\" to make a new line number\n"+
        "Type \"O\" to make a new order\n"+
        "Type \"P\" to make a new product\n"+
        "Type \"S\" to make a new sales rep\n"+
        "Type \"V\" to make a new vendor\n"+
        "Command: ")
        Create.Create(createInput,databaseCursor,database,username)

    elif(userInput=="R"):
        readInput=input("\nPlease select a table to read from\n"+
        "Type \"L\" to read from the line number table\n"+
        "Type \"O\" to read from the order table\n"+
        "Type \"P\" to read from the product table\n"+
        "Type \"S\" to read from the sales rep table\n"+
        "Type \"V\" to read from the vendor table\n"+
        "Type \"Other\" to select from a list of queries with multiple tables involved\n"+
        "Command: ")
        Read.Read(readInput,databaseCursor,database,username)

    elif(userInput=="U"):
        updateInput=input("\nPlease select what type of data you would like to update\n"+
        "Type \"L\" to make a new line number\n"+
        "Type \"O\" to make a new order\n"+
        "Type \"P\" to make a new product\n"+
        "Type \"S\" to make a new sales rep\n"+
        "Type \"V\" to make a new vendor\n"+
        "Command: ")
        Update.Update(updateInput,databaseCursor,database,username)
    
    elif(userInput=="D"):
        deleteInput=input("\nPlease select what type of data you would like to delete\n"+
        "Type \"L\" to delete a line number\n"+
        "Type \"O\" to delete a order\n"+
        "Type \"P\" to delete a product\n"+
        "Type \"S\" to delete a sales rep\n"+
        "Type \"V\" to delete a vendor\n"+
        "Command: ")
        Delete.Delete(deleteInput,databaseCursor,database,username)

    elif(userInput=="Exit"):
        print("\nExit successful")
    
    else:
        print("Invalid input. Please enter in one of the commands above")