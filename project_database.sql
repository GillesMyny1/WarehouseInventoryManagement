PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS warehouse (
warehouse_bin INTEGER PRIMARY KEY NOT NULL,
product_id INTEGER NOT NULL,
bin_quantity INTEGER NOT NULL);

CREATE TABLE IF NOT EXISTS product (
product_id INTEGER PRIMARY KEY NOT NULL,
description VARCHAR(255) NOT NULL);

CREATE TABLE IF NOT EXISTS buy_order_sheet (
buy_order_num INTEGER PRIMARY KEY NOT NULL,
origin_adrr VARCHAR(255) NOT NULL,
arrival_date VARCHAR(10) NOT NULL);

CREATE TABLE IF NOT EXISTS sell_order_sheet (
sell_order_num INTEGER PRIMARY KEY NOT NULL,
destination_addr VARCHAR(255) NOT NULL,
soldby_date VARCHAR(10) NOT NULL);

CREATE TABLE IF NOT EXISTS buy_order (
identifier INTEGER PRIMARY KEY AUTOINCREMENT,
buy_order_num INTEGER NOT NULL,
warehouse_bin INTEGER NOT NULL,
buy_prod_quantity INTEGER NOT NULL,
FOREIGN KEY (buy_order_num) REFERENCES buy_order_sheet(buy_order_num),
FOREIGN KEY (warehouse_bin) REFERENCES warehouse(warehouse_bin));

CREATE TABLE IF NOT EXISTS sell_order (
identifier INTEGER PRIMARY KEY AUTOINCREMENT,
sell_order_num INTEGER NOT NULL,
warehouse_bin INTEGER NOT NULL,
sell_prod_quantity INTEGER NOT NULL,
FOREIGN KEY (sell_order_num) REFERENCES sell_order_sheet(sell_order_num),
FOREIGN KEY (warehouse_bin) REFERENCES warehouse(warehouse_bin));

INSERT INTO buy_order_sheet VALUES (7653, '8848 Summit Ave', '2019-01-02');
INSERT INTO buy_order_sheet VALUES (6533, '712 Overlook St', '2021-12-04');
INSERT INTO buy_order_sheet VALUES (4352, '51 Orchard Court', '2020-05-10');
INSERT INTO buy_order_sheet VALUES (6754, '7042 Cross Lane', '2016-08-07');
INSERT INTO buy_order_sheet VALUES (3254, '328 Cooper Rd', '2022-03-05');
INSERT INTO buy_order_sheet VALUES (1298, '391 East Fairview St', '2019-01-02');
INSERT INTO buy_order_sheet VALUES (2387, '667 Washington St', '2021-12-04');
INSERT INTO buy_order_sheet VALUES (3476, '852 Middle River Dr', '2020-05-10');
INSERT INTO buy_order_sheet VALUES (4565, '9972 S. Mayfield St', '2016-08-07');
INSERT INTO buy_order_sheet VALUES (7654, '267 Ridgewood St', '2022-03-05');
INSERT INTO buy_order_sheet VALUES (8743, '436 State Rd', '2019-01-02');
INSERT INTO buy_order_sheet VALUES (9832, '7634 Honey Creek Ave', '2021-12-04');
INSERT INTO buy_order_sheet VALUES (0921, '859 North Windsor St', '2020-05-10');
INSERT INTO buy_order_sheet VALUES (1357, '686 NW. Beacon St', '2016-08-07');
INSERT INTO buy_order_sheet VALUES (5790, '953 Bridgeton Dr', '2022-03-05');

INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (7653, 76, 49);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (6533, 33, 78);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (4352, 18, 488);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (6754, 99, 603);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (3254, 57, 5);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (1298, 76, 18);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (2387, 33, 64);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (3476, 23, 435);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (4565, 99, 342);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (7654, 57, 43);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (8743, 76, 756);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (9832, 54, 213);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (0921, 18, 65);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (1357, 99, 23);
INSERT INTO buy_order (buy_order_num, warehouse_bin, buy_prod_quantity) VALUES (5790, 34, 876);

INSERT INTO sell_order_sheet VALUES (9797, '34 Ocean Ln', '2019-02-11');
INSERT INTO sell_order_sheet VALUES (4532, '45 Factory Rd', '2021-12-08');
INSERT INTO sell_order_sheet VALUES (6543, '76 Stone Ct', '2020-07-11');
INSERT INTO sell_order_sheet VALUES (6755, '42 Williams Rd', '2016-10-11');
INSERT INTO sell_order_sheet VALUES (1324, '3 Devon Dr', '2022-05-06');
INSERT INTO sell_order_sheet VALUES (4363, '26 Manor St', '2019-02-11');
INSERT INTO sell_order_sheet VALUES (6457, '611 Selby Rd', '2021-12-08');
INSERT INTO sell_order_sheet VALUES (8709, '91 Meadowbrook Ave', '2020-07-11');
INSERT INTO sell_order_sheet VALUES (3455, '583 Central Dr', '2016-10-11');
INSERT INTO sell_order_sheet VALUES (3244, '78 Studebaker Ave', '2022-05-06');
INSERT INTO sell_order_sheet VALUES (4563, '79 Yukon Court', '2019-02-11');
INSERT INTO sell_order_sheet VALUES (2345, '35 Greenrose St', '2021-12-08');
INSERT INTO sell_order_sheet VALUES (4765, '8660 Prairie St', '2020-07-11');
INSERT INTO sell_order_sheet VALUES (7323, '9 Lafayette Rd', '2016-10-11');
INSERT INTO sell_order_sheet VALUES (6599, '945 Chapel Ave', '2022-05-06');

INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (9797, 76, 7);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (4532, 33, 23);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (6543, 18, 54);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (6755, 99, 235);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (1324, 57, 3);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (4363, 76, 32);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (6457, 33, 65);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (8709, 23, 32);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (3455, 99, 115);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (3244, 57, 2);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (4563, 76, 7);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (2345, 54, 23);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (4765, 18, 254);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (7323, 99, 47);
INSERT INTO sell_order (sell_order_num, warehouse_bin, sell_prod_quantity) VALUES (6599, 34, 324);

INSERT INTO warehouse VALUES (76, 537750802, 777);
INSERT INTO warehouse VALUES (33, 634974359, 54);
INSERT INTO warehouse VALUES (18, 371781902, 245);
INSERT INTO warehouse VALUES (99, 540793989, 571);
INSERT INTO warehouse VALUES (57, 607417314, 43);
INSERT INTO warehouse VALUES (23, 327240301, 403);
INSERT INTO warehouse VALUES (54, 692590102, 190);
INSERT INTO warehouse VALUES (34, 795462854, 552);

INSERT INTO product VALUES (537750802, 'Apple iPhone 5S');
INSERT INTO product VALUES (634974359, 'XBox 360 Bundle');
INSERT INTO product VALUES (371781902, 'Nike Air Force 1 Black');
INSERT INTO product VALUES (540793989, 'Rolex Submariner');
INSERT INTO product VALUES (607417314, 'Backfire XS');
INSERT INTO product VALUES (327240301, 'Prada Vest Black Medium');
INSERT INTO product VALUES (692590102, 'AMD Ryzen 5600X');
INSERT INTO product VALUES (795462854, 'NVidia GTX 1060 3Gb');

COMMIT;
