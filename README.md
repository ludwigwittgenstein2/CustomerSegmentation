# Supermarket
A Prototype to improve Revenues with Supermarket data

Supermarket:
We have a data for Supermarket, And our goal is to improve Revenues by targeting Segments.

For this project, we use dunnhumby's data for a Supermarket.



About Data:

This dataset contains household level transactions over two years from a group of 2,500 households who are frequent shoppers at a retailer. It contains all of each household’s purchases, not just those from a limited number of categories. For certain households, demographic information as well as direct marketing contact history are included.


DATA TABLES: 

(a) Record connected to another table

CAMPAIGN_TABLE (1584 households mailed 30 Campaigns)
HOUSEHOLD_KEY
(a)CAMPAIGN_TABLE
DESCRIPTION

CAMPAIGN_DESC (30 Campaigns)
(a) CAMPAIGN
DESCRIPTION
START_DAY
END_DAY

COUPON_REDEMPT
434 households redeemed 556 coupons from 30 Campaigns
HOUSEHOLD_KEY
DAY
COUPON_UPC
CAMPAIGN

COUPON (1135 coupons promoted 44133 products for the 30 campaings)

CAMPAIGN
COUPON_UPC
PRODUCT_ID

HH_DEMOGRAPHIC (801 household)
HOUSEHOLD_KEY
AGE_DESC
MARITAL_STATUS_CODE
INCOME_DESC
HOMEOWNER_DESC
HH_COMP_DESC
HOUSEHOLD_SIZE_DESC
KID_CATEGORY_DESC

TRANSACTION_DATA (2500 Households shopped 92339 products)

HOUSEHOLD_KEY
BASKET_ID
DAY
PRODUCT_ID
QUANTITY
SALES_VALUE
STORE_ID
COUPON_MATCH_DISC
COUPON_DISC
RETAIL_DISC
TRANS_TIME
WEEK_NO

PRODUCT (92353 products)
PRODUCT_ID
COMMODITY_DESC
SUB_COMMODITY_DESC
MANUFACTURER
DEPARTMENT
BRAND
CURR_SIZE_OF_PRODUCT

CASUAL_DATA(68377 products)

PRODUCT_ID
STORE_ID
WEEK_NO
DISPLAY
MAILER

Code:


firstQuestion.py --
