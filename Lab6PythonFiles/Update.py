#Created by Nicholas Caballero
import prettytable
from prettytable import from_db_cursor
import datetime
def Update(updateCommandInput, databaseCursor, database,username):
    if(updateCommandInput=="L"):
        lineNumberPK=input("\nPlease enter in the order ID number and the line number in the following format:\n"+
        "order_id, line number\n"+
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

            newInfo=input("\nPlease enter all information (regardless if it's old or new) in the following format:\n"+
            "product_id, price, order_quantity"+
            "\nPlease enter in the product ID, price, and order quantity here:")

            newInfo.replace(" ", "")
            seperatedNewInfo=newInfo.split(',')

            updateStatement=("UPDATE vw_line_number"+
            " SET product_id="+seperatedNewInfo[0]+
            ", price="+seperatedNewInfo[1]+
            ", order_quantity="+seperatedNewInfo[2]+
            " WHERE order_id="+seperatedInputs[0]+" AND line_number="+seperatedInputs[1])

            databaseCursor.execute(updateStatement)
            database.commit()

            databaseCursor.execute("select*from vw_line_number WHERE order_id="+seperatedInputs[0]+" AND line_number="+seperatedInputs[1])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis is the newly-updated information stored:\n")
            print(currentInfo)

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(updateCommandInput=="O"):
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

            newInfo=input("\nPlease enter all information (regardless if it's old or new) in the following format:\n"+
            "vendor_id, sales_rep_id, 'order_date', 'estimated_arrival_date'"+
            "\nEnter in the information here: ")

            newInfo.replace(" ", "")
            seperatedNewInfo=newInfo.split(',')

            updateStatement=("UPDATE vw_order"+
            " SET vendor_id="+seperatedNewInfo[0]+
            ", sales_rep_id="+seperatedNewInfo[1]+
            ", order_date="+seperatedNewInfo[2]+
            ", estimated_arrival_date="+seperatedNewInfo[3]+
            " WHERE order_id="+seperatedInputs[0])

            databaseCursor.execute(updateStatement)
            database.commit()

            databaseCursor.execute("select*from vw_order WHERE order_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis is the newly-updated information stored:\n")
            print(currentInfo)

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")
    
    elif(updateCommandInput=="P"):
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

            newInfo=input("\nPlease enter all information (regardless if it's old or new) in the following format:\n"+
            "vendor_id, 'product_name', 'product_description', price\n"+
            "Enter in the information here: ")

            newInfo.replace(" ", "")
            seperatedNewInfo=newInfo.split(',')

            updateStatement=("UPDATE vw_product"+
            " SET vendor_id="+seperatedNewInfo[0]+
            ", product_name="+seperatedNewInfo[1]+
            ", product_description="+seperatedNewInfo[2]+
            ", price="+seperatedNewInfo[3]+
            " WHERE product_id="+seperatedInputs[0])

            databaseCursor.execute(updateStatement)
            database.commit()

            databaseCursor.execute("select*from vw_product WHERE product_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis is the newly-updated information stored:\n")
            print(currentInfo)

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(updateCommandInput=="S"):
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

            newInfo=input("\nPlease enter all information (regardless if it's old or new) in the following format:\n"+
            "'sales_rep_name', 'sales_rep_telephone_number', 'sales_rep_email', vendor_id\n"+
            "Enter in the information here: ")

            newInfo.replace(" ", "")
            seperatedNewInfo=newInfo.split(',')

            updateStatement=("UPDATE vw_sales_rep"+
            " SET sales_rep_name="+seperatedNewInfo[0]+
            ", sales_rep_telephone_number="+seperatedNewInfo[1]+
            ", sales_rep_email="+seperatedNewInfo[2]+
            ", vendor_id="+seperatedNewInfo[3]+
            " WHERE sales_rep_id="+seperatedInputs[0])

            databaseCursor.execute(updateStatement)
            database.commit()

            databaseCursor.execute("select*from vw_sales_rep WHERE sales_rep_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis is the newly-updated information stored:\n")
            print(currentInfo)

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")

    elif(updateCommandInput=="V"):
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

            newInfo=input("\nPlease enter all information (regardless if it's old or new) in the following format:\n"+
            "'vendor_name', account_payable_terms\n"+
            "Enter in the information here: ")

            newInfo.replace(" ", "")
            seperatedNewInfo=newInfo.split(',')

            updateStatement=("UPDATE vw_vendor"+
            " SET vendor_name="+seperatedNewInfo[0]+
            ", account_payable_terms="+seperatedNewInfo[1]+
            " WHERE vendor_id="+seperatedInputs[0])

            databaseCursor.execute(updateStatement)
            database.commit()

            databaseCursor.execute("select*from vw_vendor WHERE vendor_id="+seperatedInputs[0])
            currentInfo=from_db_cursor(databaseCursor)
            print("\nThis is the newly-updated information stored:\n")
            print(currentInfo)

            now=datetime.datetime.now()
            currentDateTime=now.strftime("%m/%d/%Y, %H:%M:%S")
            print("\nQueried by "+username+" on " +currentDateTime+"\n")
            
    else:
        print("\nError: Not a valid input. Please enter a valid input")