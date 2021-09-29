#Created by Nicholas Caballero
import prettytable
from prettytable import from_db_cursor
import ViewsandStoredProcedures
import datetime
def Read(readCommandInput,databaseCursor,database,username):
    if(readCommandInput=="L"):
        viewLineNumberTable="select*from vw_line_number;"
        databaseCursor.execute(viewLineNumberTable)
        lineNumberTable=from_db_cursor(databaseCursor)
        print(lineNumberTable)

        now=datetime.datetime.now()
        currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
        print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(readCommandInput=="O"):
        viewOrderTable="select*from vw_order;"
        databaseCursor.execute(viewOrderTable)
        orderTable=from_db_cursor(databaseCursor)
        print(orderTable)

        now=datetime.datetime.now()
        currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
        print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(readCommandInput=="P"):
        viewProductTable="select*from vw_product;"
        databaseCursor.execute(viewProductTable)
        productTable=from_db_cursor(databaseCursor)
        print(productTable)

        now=datetime.datetime.now()
        currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
        print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(readCommandInput=="S"):
        viewSalesRepTable="select*from vw_sales_rep;"
        databaseCursor.execute(viewSalesRepTable)
        salesRepTable=from_db_cursor(databaseCursor)
        print(salesRepTable)

        now=datetime.datetime.now()
        currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
        print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(readCommandInput=="V"):
        viewVendorTable="select*from vw_vendor;"
        databaseCursor.execute(viewVendorTable)
        vendorTable=from_db_cursor(databaseCursor)
        print(vendorTable)

        now=datetime.datetime.now()
        currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
        print("\nQueried by "+username+" on " +currentDateTime+"\n")
        
    elif(readCommandInput=="Other"):
        ViewsandStoredProcedures.Read(databaseCursor,database,username)
    else:
        print("\nError: Not a valid input. Please enter a valid input")