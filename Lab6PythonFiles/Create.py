#Created by Nicholas Caballero
import datetime
import prettytable
from prettytable import from_db_cursor
def Create(createCommandInput,databaseCursor,database,username):
    if(createCommandInput=="L"):
        lineNumberInput=input("\nEnter the new line number in the following format:\n"+
        "order_id, line_number, product_id, price, order_quantity\n"+
        "Enter new line number here: ")

        lineNumberInput.replace(" ", "")
        seperatedInputs=lineNumberInput.split(',')

        if(len(seperatedInputs)!=5):
            print("Error: Too few or too many elements.\n"+
            "Please check that your input is correct and try again")
        else:
            insertStatement=("insert into vw_line_number select "+lineNumberInput+";")
            databaseCursor.execute(insertStatement)
            database.commit()

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

            databaseCursor.execute("\nselect*from vw_line_number WHERE order_id="+seperatedInputs[0]+" AND line_number="+seperatedInputs[1])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis shows that the data has been added:\n")
            print(currentInfo)
            
    elif(createCommandInput=="O"):
        orderInput=input("\nEnter the new order in the following format:\n"+
        "order_id, vendor_id, sales_rep_id, 'order_date'(year/month/day), 'estimated_arrival_date'(year/month/day)\n"+
        "Enter new order here: ")

        orderInput.replace(" ", "")
        seperatedInputs=orderInput.split(',')

        if(len(seperatedInputs)!=5):
            print("Error: Too few or too many elements.\n"+
            "Please check that your input is correct and try again")
        else:
            insertStatement=("insert into vw_order select "+seperatedInputs[0]+","+seperatedInputs[1]+","+seperatedInputs[2]+","+seperatedInputs[3]+","+seperatedInputs[4]+";")
            databaseCursor.execute(insertStatement)
            database.commit()

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

            databaseCursor.execute("select*from vw_order WHERE order_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis shows that the data has been added:\n")
            print(currentInfo)

    elif(createCommandInput=="P"):
        productInput=input("\nEnter the new product in the following format:\n"+
        "product_id, vendor_id, 'product_name', 'product_description', price\n"+
        "Enter new product here: ")

        productInput.replace(" ", "")
        seperatedInputs=productInput.split(',')

        if(len(seperatedInputs)!=5):
            print("Error: Too few or too many elements.\n"+
            "Please check that your input is correct and try again")
        else:
            insertStatement=("insert into vw_product select "+productInput+";")
            databaseCursor.execute(insertStatement)
            database.commit()

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

            databaseCursor.execute("select*from vw_product WHERE product_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis shows that the data has been added:\n")
            print(currentInfo)

    elif(createCommandInput=="S"):
        salesRepInput=input("\nEnter the new order in the following format:\n"+
        "sales_rep_id, 'sales_rep_name', 'sales_rep_telephone_number', 'sales_rep_email', vendor_id\n"+
        "Enter new sales rep here: ")

        salesRepInput.replace(" ", "")
        seperatedInputs=salesRepInput.split(',')

        if(len(seperatedInputs)!=5):
            print("Error: Too few or too many elements.\n"+
            "Please check that your input is correct and try again")
        else:
            insertStatement=("insert into vw_sales_rep select "+salesRepInput+";")
            databaseCursor.execute(insertStatement)
            database.commit()

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

            databaseCursor.execute("select*from vw_sales_rep WHERE sales_rep_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis shows that the data has been added:\n")
            print(currentInfo)

    elif(createCommandInput=="V"):
        vendorInput=input("\nEnter the new vendor in the following format:\n"+
        "vendor_id, 'vendor_name', account_payable_terms\n"+
        "Enter new vendor here: ")

        vendorInput.replace(" ", "")
        seperatedInputs=vendorInput.split(',')

        if(len(seperatedInputs)!=3):
            print("Error: Too few or too many elements.\n"+
            "Please check that your input is correct and try again")
        else:
            insertStatement=("insert into vw_vendor select "+vendorInput+";")
            databaseCursor.execute(insertStatement)
            database.commit() 

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

            databaseCursor.execute("select*from vw_vendor WHERE vendor_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis shows that the data has been added:\n")
            print(currentInfo)


    else:
        print("\nError: Not a valid input. Please enter a valid input")  