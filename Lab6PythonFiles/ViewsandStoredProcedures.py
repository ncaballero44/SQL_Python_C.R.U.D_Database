#Created by Nicholas Caballero
import prettytable
from prettytable import from_db_cursor
import datetime

def Read(databaseCursor,database,username):
    commandInput=input("\nType \"1\" to see a list of sales reps and their contact info ordered by vendor\n"+ #vw_vendor_contacts_nc
    "Type \"2\" to see a list of all products and the total in sales by sales rep\n"+ #vw_product_sales_by_rep9_nc
    "Type \"3\" to see a list of vendors that sell a specific product sorted from lowest to highest price\n"+ #sp_vendors_by_product3_nc
    "Type \"4\" to see a list of orders from a particular vendor that fall between a start date and an end date sorted by order date newest to oldest\n"+#sp_get_vendor_orders_by_date10_nc
    "Please type your command here: ") 
    if(commandInput=="1"):
        databaseCursor.execute("SELECT * from vw_vendor_contacts_nc;")
        viewResult=from_db_cursor(databaseCursor)
        print(viewResult)

        now=datetime.datetime.now()
        currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
        print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(commandInput=="2"):
        databaseCursor.execute("select * from vw_product_sales_by_rep9_nc;")
        viewResult=from_db_cursor(databaseCursor)
        print(viewResult)

        now=datetime.datetime.now()
        currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
        print("\nQueried by "+username+" on " +currentDateTime+"\n")
        
    elif(commandInput=="3"):
        databaseCursor.execute("select distinct product_name from product_nc order by product_name;")
        viewResult=from_db_cursor(databaseCursor)
        print(viewResult)
        procedureInput=input("\nPlease select a product from the list above and type it exactly as listed above"+
        "\nProduct Name: ")
        databaseCursor.execute("CALL sp_vendors_by_product3_nc(\""+procedureInput+"\");")
        procedureResult=from_db_cursor(databaseCursor)
        print(procedureResult)

        now=datetime.datetime.now()
        currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
        print("\nQueried by "+username+" on " +currentDateTime+"\n")
    
    elif(commandInput=="4"):
        databaseCursor.execute("select vendor_id, vendor_name from vendor_nc order by vendor_id")
        viewResult=from_db_cursor(databaseCursor)
        print(viewResult)
        procedureInput=input("\nPlease select a vendor from above and type in the corresponding vendor_id as well as the start date and end date in the following format:"+
        "\nvendor_id, \"start date\" (year/month/day), \"end date\" (year/month/day)"+
        "\nEnter in your input here: ")
        databaseCursor.execute("CALL sp_get_vendor_orders_by_date10_nc("+procedureInput+");")
        procedureResult=from_db_cursor(databaseCursor)
        print(procedureResult)

        now=datetime.datetime.now()
        currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
        print("\nQueried by "+username+" on " +currentDateTime+"\n")

    else:
        print("Invalid input. Please type in a valid input")