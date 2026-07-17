CREATE OR REPLACE WAREHOUSE ecommerce_wh
WITH
WAREHOUSE_SIZE='XSMALL'
AUTO_SUSPEND=60
AUTO_RESUME=TRUE;
CREATE OR REPLACE DATABASE ecommerce_db;
USE DATABASE ecommerce_db;

CREATE OR REPLACE SCHEMA analytics;

USE WAREHOUSE ecommerce_wh;
USE DATABASE ecommerce_db;
USE SCHEMA analytics;

SHOW WAREHOUSES;
SHOW DATABASES;
SHOW SCHEMAS;

CREATE OR REPLACE FILE FORMAT parquet_format
TYPE = PARQUET;
CREATE OR REPLACE STAGE gold_stage
URL='s3://prithiv-ecommerce-raw-751835847273/gold/'
CREDENTIALS=(

)
FILE_FORMAT=parquet_format;

LIST @gold_stage;
CREATE OR REPLACE TABLE gold_sales_by_product (
    PRODUCT STRING,
    TOTAL_REVENUE FLOAT,
    TOTAL_ORDERS NUMBER
);

COPY INTO gold_sales_by_product
FROM @gold_stage/sales_by_product/
FILE_FORMAT = (TYPE = PARQUET)
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;
LIST @gold_stage/sales_by_product;

COPY INTO gold_sales_by_product
FROM @gold_stage/sales_by_product
PATTERN='.*\.parquet'
FILE_FORMAT = (TYPE = PARQUET)
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;
CREATE OR REPLACE TABLE gold_sales_by_city (
    CITY STRING,
    TOTAL_REVENUE FLOAT,
    TOTAL_ORDERS NUMBER
);
COPY INTO gold_sales_by_city
FROM @gold_stage/sales_by_city
PATTERN='.*\.parquet'
FILE_FORMAT=(TYPE=PARQUET)
MATCH_BY_COLUMN_NAME=CASE_INSENSITIVE;
CREATE OR REPLACE TABLE gold_daily_sales (
    ORDER_DATE DATE,
    DAILY_REVENUE FLOAT,
    TOTAL_ORDERS NUMBER
);
COPY INTO gold_daily_sales
FROM @gold_stage/daily_sales
PATTERN='.*\.parquet'
FILE_FORMAT=(TYPE=PARQUET)
MATCH_BY_COLUMN_NAME=CASE_INSENSITIVE;
CREATE OR REPLACE TABLE gold_payment_summary (
    PAYMENT_METHOD STRING,
    TOTAL_ORDERS NUMBER,
    TOTAL_REVENUE FLOAT
);
COPY INTO gold_payment_summary
FROM @gold_stage/payment_summary
PATTERN='.*\.parquet'
FILE_FORMAT=(TYPE=PARQUET)
MATCH_BY_COLUMN_NAME=CASE_INSENSITIVE;

SELECT * FROM gold_sales_by_city;

SELECT * FROM gold_daily_sales;

SELECT * FROM gold_payment_summary;
