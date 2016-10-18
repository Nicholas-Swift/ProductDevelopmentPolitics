-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2016-10-18 21:45:33.213

-- tables
-- Table: client
CREATE TABLE client (
    id int NOT NULL,
    full_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    CONSTRAINT client_pk PRIMARY KEY (id)
);

-- Table: counciler
CREATE TABLE counciler (
    id int NOT NULL,
    party_id int NOT NULL,
    ward int NOT NULL,
    telephone int NOT NULL,
    email varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    CONSTRAINT counciler_pk PRIMARY KEY (id)
);

-- Table: party
CREATE TABLE party (
    id int NOT NULL,
    name varchar(255) NOT NULL,
    CONSTRAINT party_pk PRIMARY KEY (id)
);

-- Table: sub_to_ward
CREATE TABLE sub_to_ward (
    id int NOT NULL,
    ward_id int NOT NULL,
    CONSTRAINT sub_to_ward_pk PRIMARY KEY (id)
);

-- Table: ward
CREATE TABLE ward (
    id int NOT NULL,
    counciler_id int NOT NULL,
    sub_to_ward_id int NOT NULL,
    CONSTRAINT ward_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: client_order (table: sub_to_ward)
ALTER TABLE sub_to_ward ADD CONSTRAINT client_order FOREIGN KEY client_order (ward_id)
    REFERENCES client (id);

-- Reference: product_category_product (table: counciler)
ALTER TABLE counciler ADD CONSTRAINT product_category_product FOREIGN KEY product_category_product (party_id)
    REFERENCES party (id);

-- Reference: product_order_item (table: ward)
ALTER TABLE ward ADD CONSTRAINT product_order_item FOREIGN KEY product_order_item (counciler_id)
    REFERENCES counciler (id);

-- Reference: ward_sub_to_ward (table: ward)
ALTER TABLE ward ADD CONSTRAINT ward_sub_to_ward FOREIGN KEY ward_sub_to_ward (sub_to_ward_id)
    REFERENCES sub_to_ward (id);

-- End of file.

