SET GLOBAL log_bin_trust_function_creators = 1;

DELIMITER //

CREATE FUNCTION query_runner(myname varchar(20)) RETURNS varchar(75)
BEGIN
DECLARE output varchar(75);
SET output=concat('Queried by ', myname, ' on ', now());
return output;
END //

DELIMITER ;

SELECT query_runner('NicholasCaballero') as "QueryRunner/Date";

CREATE VIEW vw_vendor_contacts_nc as
SELECT
	sales_rep_name as "Sales Rep",
    vendor_name as "Vendor Name",
    sales_rep_email as "Email",
    sales_rep_telephone_number as "Telephone",
    query_runner('Nicholas Caballero') as "Query Runner / Date"
FROM
	vendor_nc,sales_rep_nc
WHERE
	vendor_nc.vendor_id=sales_rep_nc.vendor_id
order by vendor_name;

SELECT * from vw_vendor_contacts_nc;

CREATE VIEW vw_products_due28_nc as
SELECT
	product_nc.product_name as "Product Name",
    order_nc.estimated_arrival_date as "Est. Arrival Date",
    vendor_nc.vendor_name as "Vendor Name",
    sales_rep_nc.sales_rep_name as "Sales Rep",
    sales_rep_nc.sales_rep_email as "Sales Rep Email",
    sales_rep_nc.sales_rep_telephone_number as "Telephone",
    query_runner('Nicholas Caballero') as "Query Runner / Date"
FROM
	product_nc, order_nc, vendor_nc, sales_rep_nc, line_number_nc
WHERE
	order_nc.estimated_arrival_date > '2020-09-29'
    AND product_nc.product_id=line_number_nc.product_id
    AND vendor_nc.vendor_id=sales_rep_nc.vendor_id
    AND line_number_nc.order_id=order_nc.order_id
    AND line_number_nc.product_id=product_nc.product_id
    AND order_nc.sales_rep_id=sales_rep_nc.sales_rep_id
    
    
order by estimated_arrival_date;

select * from vw_products_due28_nc;
	

create view vw_product_sales_by_rep9_nc as
SELECT
	productTable.product_name as "Product Name",
    salesRepTable.sales_rep_name as "Sales Rep",
    vendorTable.vendor_name as "Vendor Name",
    round(sum(productTable.price * lineNumber.order_quantity),2) as "Sales Total by Product",
    query_runner('Nicholas Caballero') as "Query Runner / Date"
FROM line_number_nc as lineNumber

join order_nc as orderTable on lineNumber.order_id=orderTable.order_id

join sales_rep_nc as salesRepTable on orderTable.sales_rep_id=salesRepTable.sales_rep_id

join product_nc as productTable on productTable.product_id=lineNumber.product_id

join vendor_nc as vendorTable on vendorTable.vendor_id=salesRepTable.vendor_id

GROUP BY lineNumber.product_id;

select * from vw_product_sales_by_rep9_nc;

create view vw_sales_rep_totals8_nc as
SELECT
	`Sales Rep`,
    `Vendor Name`,
    `Sales Total by Product` as "Total Sales",
    query_runner('Nicholas Caballero') as "Query Runner / Date"
FROM vw_product_sales_by_rep9_nc
GROUP BY `Sales Rep`
ORDER BY `Total Sales` DESC;

select *from vw_sales_rep_totals8_nc;

create view vw_upcoming_payments_2nc as
SELECT
	vendorTable.vendor_name as "Vendor Name",
    date_add(orderTable.order_date, INTERVAL vendorTable.account_payable_terms DAY) as "Payment Due Date",
    (lineNumber.price*lineNumber.order_quantity) as "Payment Due",
    orderTable.order_id as "Order ID",
    orderTable.order_date as "Order Date",
    query_runner('Nicholas Caballero') as "Query Runner / Date"
FROM line_number_nc as lineNumber

join order_nc as orderTable on lineNumber.order_id=orderTable.order_id

join sales_rep_nc as salesRepTable on orderTable.sales_rep_id=salesRepTable.sales_rep_id

join product_nc as productTable on productTable.product_id=lineNumber.product_id

join vendor_nc as vendorTable on vendorTable.vendor_id=salesRepTable.vendor_id;

select * from vw_upcoming_payments_2nc;

DELIMITER //
create procedure sp_vendors_by_product3_nc (productName varchar(64))
BEGIN
	SELECT
		vendorTable.vendor_name as "Vendor Name",
        productTable.product_name as "Product Name",
        productTable.price as "Product Price",
        productTable.product_description as "Product Description",
        productTable.product_id as "Product ID",
        query_runner('Nicholas Caballero') as "Query Runner / Date"
        
FROM line_number_nc as lineNumber

join order_nc as orderTable on lineNumber.order_id=orderTable.order_id

join sales_rep_nc as salesRepTable on orderTable.sales_rep_id=salesRepTable.sales_rep_id

join product_nc as productTable on productTable.product_id=lineNumber.product_id

join vendor_nc as vendorTable on vendorTable.vendor_id=salesRepTable.vendor_id	

WHERE 
	productTable.product_name=productName
group by vendorTable.vendor_name;
END	//
DELIMITER ;
CALL sp_vendors_by_product3_nc("Airframe fasteners");

DELIMITER //
create procedure sp_update_product_price23_nc (IN productID INT, IN newPrice decimal(4,2))
BEGIN
DECLARE output varchar(128);
DECLARE tempID INT;
SELECT product_id INTO tempID
from product_nc
WHERE product_nc.product_id=productID;
IF tempID=productID THEN
	UPDATE product_nc
    SET price=newPrice
    WHERE product_nc.product_id=productID;
    SET output=concat('Price updated for product id: ' , productID , ' to ' , newPrice);
ELSE
	SET output=concat('Product does not exist. Please check product id');
END IF;
SELECT
	output as "Response Code";
END//
DELIMITER ;

CALL  sp_update_product_price23_nc (1002, 4.89);

DELIMITER //
create procedure sp_get_vendor_orders_by_date10_nc(IN vendorID INT, IN startDate date, IN endDate date)
BEGIN
SELECT 
	orderTable.order_id as "Order ID",
    vendorTable.vendor_name as "Vendor Name",
    lineNumber.line_number as "Line Item",
    productTable.product_name as "Product Name",
    productTable.price as "Sales Price",
    lineNumber.order_quantity as "Quantity",
    (productTable.price*lineNumber.order_quantity) as "Line Item Cost",
    orderTable.order_date as "Order Date",
    orderTable.estimated_arrival_date as "Est. Arrival"
FROM line_number_nc as lineNumber, order_nc as orderTable, sales_rep_nc as salesRepTable, product_nc as productTable,vendor_nc as vendorTable
WHERE 
	vendorTable.vendor_id=vendorID
    AND orderTable.order_date>=startDate
    AND orderTable.order_date<=endDate
    AND vendorTable.vendor_id=salesRepTable.vendor_id
    AND lineNumber.order_id=orderTable.order_id
	AND lineNumber.product_id=productTable.product_id
group by lineNumber.product_id,lineNumber.line_number
order by orderTable.order_date;
END//
DELIMITER ;
CALL sp_get_vendor_orders_by_date10_nc(1001,"2020/09/03",now());

DELIMITER //
create procedure sp_insert_sales_rep23_nc (IN SalesRepID INT, IN SalesRepName varchar(64), IN PhoneNumber varchar(15), IN Email varchar(64), IN VendorID INT)
BEGIN
	DECLARE output varchar(128);
	DECLARE tempVendorID INT;
    DECLARE tempSalesRepID INT;
    SET tempVendorID=NULL;
	SELECT vendor_id into tempVendorID
    FROM vendor_nc
    WHERE vendor_nc.vendor_id=VendorID;
    SELECT sales_rep_id into tempSalesRepID
    from sales_rep_nc
    WHERE sales_rep_nc.sales_rep_id=SalesRepID;
	CASE
		WHEN tempVendorID IS NULL THEN SET output=concat('Vendor does not exist. Please check vendor id.');
        WHEN tempSalesRepID=SalesRepID THEN SET output=concat('Sales Rep already exists. Please use an alternate sales rep id');
        ELSE insert into sales_rep_nc(sales_rep_id, sales_rep_name, sales_rep_telephone_number, sales_rep_email,vendor_id) values(SalesRepID,SalesRepName,PhoneNumber,Email,VendorID);
	END CASE;
    IF output IS NULL THEN SET output=concat('Sales rep added');
    END IF;
    SELECT output as "Response Code";
END//
DELIMITER ;

CALL sp_insert_sales_rep23_nc(9002276, "Nick Caballero", "123-456-7890", "me@email.com", 9002);	

DELIMITER //
create procedure sp_vendors_by_product109_nc(IN productName varchar(64))
BEGIN
SELECT 
orderTable.order_id as "Order ID",
lineNumber.line_number as "Line Number",
vendorTable.vendor_id as "Vendor ID",
vendorTable.vendor_name as "Vendor Name",
orderTable.sales_rep_id as "Sales Rep ID",
salesRepTable.sales_rep_name as "Sales Rep",
salesRepTable.sales_rep_telephone_number as "Sales Rep Telephone",
salesRepTable.sales_rep_email as "Sales Rep Email",
lineNumber.product_id as "Product ID",
productTable.product_name as "Product Name",
productTable.product_description as "Product Description",
productTable.price as "Price",
lineNumber.order_quantity as "Order Quantity",
(productTable.price*lineNumber.order_quantity) as "Cost Per Order",
vendorTable.account_payable_terms as "Account Payable Terms",
orderTable.order_date as "Order Date",
orderTable.estimated_arrival_date as "Estimated Arrival Date",
query_runner('Nicholas Caballero') as "Query Runner / Date"
FROM line_number_nc as lineNumber, order_nc as orderTable, sales_rep_nc as salesRepTable, product_nc as productTable,vendor_nc as vendorTable
WHERE
	productTable.product_name=productName
	AND productTable.product_id=lineNumber.product_id
    AND vendorTable.vendor_id=salesRepTable.vendor_id
    AND lineNumber.order_id=orderTable.order_id
    AND lineNumber.product_id=productTable.product_id
    AND orderTable.sales_rep_id=salesRepTable.sales_rep_id
order by productTable.price;
END//   
DELIMITER ;
CALL sp_vendors_by_product109_nc("Bolt-nut package");

create view vw_schema_routines5_nc as
SELECT
	dataDictionary.TABLE_NAME as "Table Name",
    routineInfo.ROUTINE_NAME as "Routine Name",
    routineInfo.ROUTINE_TYPE as "Type",
    routineInfo.DATA_TYPE as "Return Type",
    routineInfo.ROUTINE_DEFINITION as "Definition",
    query_runner('Nicholas Caballero') as "Query Runner / Date"
FROM `INFORMATION_SCHEMA`.`TABLES` as dataDictionary, `INFORMATION_SCHEMA`.`ROUTINES` as routineInfo
group by routineInfo.ROUTINE_NAME;		

select * from vw_schema_routines5_nc;

create view vw_schema_routines7_nc as
SELECT
	viewInfo.TABLE_NAME as "View Name",
    viewInfo.TABLE_SCHEMA as "Schema",
    viewInfo.VIEW_DEFINITION as "View Definition",
    viewInfo.IS_UPDATABLE as "Is Updatable",
    query_runner('Nicholas Caballero') as "Query Runner / Date"
FROM `INFORMATION_SCHEMA`.`VIEWS` as viewInfo
group by viewInfo.TABLE_NAME;   

select*from vw_schema_routines7_nc;

create view vw_schema_tables_nc as
select 
tableInfo.TABLE_SCHEMA as "Table Schema",
tableInfo.TABLE_NAME as "Table Name",
tableInfo.TABLE_TYPE as "Type",
tableInfo.ENGINE as "Engine",
tableInfo.CREATE_TIME as "Created on",
query_runner('Nicholas Caballero') as "Query Runner / Date"
 from `INFORMATION_SCHEMA`.`TABLES` as tableInfo 
 where 
 tableInfo.TABLE_Schema='lab3and4'
 AND tableInfo.TABLE_TYPE='BASE TABLE';
 
select*from vw_schema_tables2_nc;

create view vw_line_number as
SELECT
	order_id,
    line_number,
    product_id,
    price,
    order_quantity
FROM
	line_number_nc;
--     
select*from vw_line_number;

create view vw_order as
SELECT
	order_id,
    vendor_id,
    sales_rep_id,
    order_date,
    estimated_arrival_date
FROM
	order_nc;

select*from vw_order;

create view vw_product as
SELECT
	product_id,
    vendor_id,
    product_name,
    product_description,
    price
FROM
	product_nc;

select*from vw_product;

create view vw_sales_rep as
SELECT
	sales_rep_id,
    sales_rep_name,
    sales_rep_telephone_number,
    sales_rep_email,
    vendor_id
FROM
	sales_rep_nc;

select*from vw_sales_rep;

create view vw_vendor as
SELECT
	vendor_id,
    vendor_name,
    account_payable_terms
FROM
	vendor_nc;
    
select*from vw_vendor;