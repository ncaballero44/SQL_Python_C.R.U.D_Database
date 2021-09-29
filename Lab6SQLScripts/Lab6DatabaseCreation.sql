
create table `vendor_nc`(
`vendor_id` INT(8) primary key,
`vendor_name` varchar(128) not null,
`account_payable_terms` INT(4) not null,
`nicholas_caballero` int(1)
)ENGINE=InnoDB;

create table `product_nc`(
`product_id` INT(8) primary key,
`vendor_id` INT(8) not null,
foreign key(vendor_id) references vendor_nc(vendor_id),
`product_name` varchar(128) not null,
`product_description` varchar(512) not null,
`price` decimal(6,2) not null,
`nicholas_caballero` int(1)
)ENGINE=InnoDB;

create table `sales_rep_nc`(
`sales_rep_id` INT(7) primary key,
`sales_rep_name` varchar(64) not null,
`sales_rep_telephone_number` varchar(15) not null,
`sales_rep_email` varchar(64) not null,
`vendor_id` INT(4) not null,
foreign key(vendor_id) references vendor_nc(vendor_id),
`nicholas_caballero` int(1)
)ENGINE=InnoDB;

create table `order_nc`(
`order_id` INT(5) primary key,
`vendor_id` INT(4) not null,
foreign key(vendor_id) references vendor_nc(vendor_id),
`sales_rep_id` INT(7) not null,
foreign key(sales_rep_id) references sales_rep_nc(sales_rep_id),
`order_date` date not null,
`estimated_arrival_date` date not null,
`nicholas_caballero` int(1)
)ENGINE=InnoDB;

create table `line_number_nc`(
`order_id` INT(5) not null,
foreign key(order_id) references order_nc(order_id),
`line_number` INT(1) not null,
primary key(order_id,line_number),
`product_id` INT(4) not null,
foreign key(product_id) references product_nc(product_id),
`price` float(7,2) not null,
`order_quantity` INT(7) not null,
`nicholas_caballero` int(1)
)ENGINE=InnoDB;

create table `user_and_password`(
`user` varchar(32),
`password` varchar(32),
`nicholas_caballero` int(1)
)ENGINE=InnoDB;

insert into user_and_password(user, password) values('nicholas.caballero363', 'letmein420');
insert into user_and_password(user, password) values('professor', 'letmein420');
select*from user_and_password;
select*from vendor_nc;
select*from line_number_nc;
select*from order_nc;
select*from product_nc; -- where product_id=5417

insert into vw_vendor select 1010, 'test', 27;
insert into vw_order select 10062,1007,9002231,date '2020/09/22',date '2020/10/09';
select*from vendor_nc;
select*from order_nc;
select*from vw_line_number;
select distinct product_name from product_nc order by product_name;
select vendor_id, vendor_name from vendor_nc order by vendor_id;

UPDATE vw_vendor SET vendor_name='test2', account_payable_terms=28 WHERE vendor_id=1010;
select*from vendor_nc;

UPDATE vw_line_number
SET product_id=9967, price=0.98, order_quantity=606
WHERE order_id=10061 AND line_number=4;

UPDATE vw_line_number SET product_id=9967, price=0.98, order_quantity=607 WHERE order_id=10061 AND line_number=4;
select*from vw_line_number;

UPDATE vw_product SET vendor_id=1001, product_name='Airframe fasteners', product_description='Airframe fasteners by Hulkey Fasteners', price=4.87 WHERE product_id=1122;
UPDATE vw_product SET vendor_id=1001, product_name='Airframe fasteners', product_description='Airframe fasteners by Hulkey Fasteners', price=4.89 WHERE product_id=1122;
select*from product_nc WHERE product_id=1122;

DELETE FROM vw_vendor WHERE vendor_id=1011;
select*from vendor_nc;

insert into product_nc(product_id,vendor_id,product_name,product_description,price)
values(9999,1001,'Airframe fasteners','Airframe fasteners by Hulkey Fasteners',4.88);

insert into sales_rep_nc(sales_rep_id, sales_rep_name, sales_rep_telephone_number, sales_rep_email,vendor_id)
values(9002262,'Nancy Woodruff','923-452-3822','nancy@durrable.com',1002);


select*from vendor_nc


