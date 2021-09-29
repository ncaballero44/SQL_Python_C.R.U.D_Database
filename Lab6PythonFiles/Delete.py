#Created by Nicholas Caballero
import prettytable
from prettytable import from_db_cursor
import datetime
def Delete(deleteCommandInput, databaseCursor, database,username):
    if(deleteCommandInput=="L"):
        lineNumberPK=input("\nPlease enter in the order ID number and the line number in the following format:\n"+
        "order_id, line_number\n"+
        "Please enter in the order ID and the line number here: ")

        lineNumberPK.replace(" ", "")
        seperatedInputs=lineNumberPK.split(',')
        if(len(seperatedInputs)!=2):
            print("Error: Too few or too many elements.\n"+
            "Please check that your input is correct and try again")
        else:
            databaseCursor.execute("select*from vw_line_number WHERE order_id="+seperatedInputs[0]+" AND line_number="+seperatedInputs[1])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis is the current information stored:\n")
            print(currentInfo)

            deleteStatement=("DELETE FROM vw_line_number WHERE order_id="+seperatedInputs[0]+" AND line_number="+seperatedInputs[1])
            
            databaseCursor.execute(deleteStatement)
            database.commit()

            databaseCursor.execute("select*from vw_line_number WHERE order_id="+seperatedInputs[0]+" AND line_number="+seperatedInputs[1])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis shows that the data has been deleted:\n")
            print(currentInfo)

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(deleteCommandInput=="O"):
        orderPK=input("\nPlease enter in the order ID number here: ")

        orderPK.replace(" ", "")
        seperatedInputs=orderPK.split(',')

        if(len(seperatedInputs)!=1):
            print("Error: Too few or too many elements.\n"+
            "Please check that your input is correct and try again")
        else:
            databaseCursor.execute("select*from vw_order WHERE order_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis is the current information stored:\n")
            print(currentInfo)

            deleteStatement=("DELETE FROM vw_order WHERE order_id="+seperatedInputs[0])

            databaseCursor.execute(deleteStatement)
            database.commit()

            databaseCursor.execute("select*from vw_order WHERE order_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis shows that the data has been deleted:\n")
            print(currentInfo)

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(deleteCommandInput=="P"):
        productPK=input("Please enter in the product ID number here:")

        productPK.replace(" ", "")
        seperatedInputs=productPK.split(',')

        if(len(seperatedInputs)!=1):
            print("Error: Too few or too many elements.\n"+
            "Please check that your input is correct and try again")
        else:
            databaseCursor.execute("select*from vw_product WHERE product_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis is the current information stored:\n")
            print(currentInfo)

            deleteStatement=("DELETE FROM vw_product WHERE product_id="+seperatedInputs[0])

            databaseCursor.execute(deleteStatement)
            database.commit()

            databaseCursor.execute("select*from vw_product WHERE product_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis shows that the data has been deleted:\n")
            print(currentInfo)

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(deleteCommandInput=="S"):
        salesRepPK=input("Please enter in the sales rep ID number here:")

        salesRepPK.replace(" ", "")
        seperatedInputs=salesRepPK.split(',')

        if(len(seperatedInputs)!=1):
            print("Error: Too few or too many elements.\n"+
            "Please check that your input is correct and try again")
        else:
            databaseCursor.execute("select*from vw_sales_rep WHERE sales_rep_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis is the current information stored:\n")
            print(currentInfo)

            deleteStatement=("DELETE FROM vw_sales_rep WHERE sales_rep_id="+seperatedInputs[0])

            databaseCursor.execute(deleteStatement)
            database.commit()

            databaseCursor.execute("select*from vw_sales_rep WHERE sales_rep_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis shows that the data has been deleted:\n")
            print(currentInfo)

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(deleteCommandInput=="V"):
        vendorPK=input("Please enter in the vendor ID number here:")

        vendorPK.replace(" ", "")
        seperatedInputs=vendorPK.split(',')

        if(len(seperatedInputs)!=1):
            print("Error: Too few or too many elements.\n"+
            "Please check that your input is correct and try again")
        else:
            databaseCursor.execute("select*from vw_vendor WHERE vendor_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis is the current information stored:\n")
            print(currentInfo)

            deleteStatement=("DELETE FROM vw_vendor WHERE vendor_id="+seperatedInputs[0])

            databaseCursor.execute(deleteStatement)
            database.commit()

            databaseCursor.execute("select*from vw_vendor WHERE vendor_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis shows that the data has been deleted:\n")
            print(currentInfo)

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

    else:
        print("\nError: Not a valid input. Please enter a valid input")
