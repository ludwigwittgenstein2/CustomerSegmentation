# Supermarket
We build a Django prototype in Python to improve revenues for Supermarket data.

Our Dataset has information about product details, purchases, demographics, coupons. Using this, our goal is to improve revenues by targeting Segments in the Dataset.

We use dunnhumby's data for a Supermarket.

___________________________________________________________

#### Data Set:

This dataset contains household level transactions over two years from a group of 2,500 households who are frequent shoppers at a retailer. It contains all of each household’s purchases, not just those from a limited number of categories. For certain households, demographic information as well as direct marketing contact history are included.

Below is the link for whole data-Set:

* [CSV-Files]  (https://www.dropbox.com/sh/6lz05ehkt31x81j/AADxV_STvuCwDujql3VwarGja?dl=0)
* [YAML-FILES](https://www.dropbox.com/sh/lz522q4z2119vh2/AACtNhemZOf4EtCojHccSHBBa?dl=0)

--------------------------------------------------------------------------------------------------

## DATA TABLES:
The following contains the structure of the Dataset, which we used for the whole prototype.

We use (a) to denote that a record is connected to another table.

--------------
##### CAMPAIGN_TABLE
(1584 households mailed 30 Campaigns)

This table lists the campaigns received by each household in the study. Each household received a different set of campaigns.
File: campaign_table.csv
```
HOUSEHOLD_KEY -- Uniquely identifies each household

(a)CAMPAIGN_TABLE -- Uniquely identifies each campaign. Ranges 1-30

DESCRIPTION -- Type of campaign(TypeA, TypeB or TypeC )
```

--------------
##### CAMPAIGN_DESC
This table gives the length of time for which a campaign runs. So, any coupons received as part of a campaign are valid within the dates contained in this table.
(30 Campaigns)

*File: campaign_desc.csv*
```
(a)CAMPAIGN -- Uniquely identifies each campaign. Ranges 1-30

DESCRIPTION -- Type of Campaign(TypeA, TypeB, TypeC)

START_DAY -- Start Date of Campaign

END_DAY -- End Date of Campaign
```

--------------
#####  COUPON_REDEMPT
(434 households redeemed 556 coupons from 30 Campaigns)

This table identifies the coupons that each household redeemed.

*File: coupon_redempt.csv*


```
HOUSEHOLD_KEY -- Uniquely identifies each household

DAY -- Day when transaction occurred

COUPON_UPC -- Uniquely identifies each coupon

CAMPAIGN -- Uniquely identifies each campaign

```

--------------
#####  COUPON
(1135 coupons promoted 44133 products for the 30 campaigns)

This table lists all the coupons sent to customers as a part of a campaign, as well as the products for which each coupon is redeemable. Some coupons are redeemable for multiple products. One example is a coupon for any private label frozen vegetable.

For campaign TypeA, this table provides pool of possible coupons. Each customer participating in a TypeA campaign received 16 coupons out of the pool. The 16 coupons were selected based on the customer's prior purchase behavior. Identifying the specific 16 coupons that each customer received is outside the scope.

*File: coupon.csv*

```
CAMPAIGN -- Uniquely identifies each campaign. Ranges 1-30

COUPON_UPC -- Uniquely identifies each coupon( unique to household and campaign)

PRODUCT_ID -- Uniquely identifies each product

```
___________________________________________
##### HH_DEMOGRAPHIC
(801 household)
This table contains demographic information for a portion of household.



*File: hh_demographic.csv*
```
HOUSEHOLD_KEY -- Uniquely Identifies each household

AGE_DESC -- Estimated age range

MARITAL_STATUS_CODE -- Marital Status (A - Married, B- Single, U-Unknown)

INCOME_DESC -- Household income

HOMEOWNER_DESC -- Homeowner, renter

HH_COMP_DESC -- Household composition

HOUSEHOLD_SIZE_DESC -- Size of household up to 5+

KID_CATEGORY_DESC -- Number of children present up to 3+
```
___________________________________________
##### TRANSACTION_DATA.csv
(2500 Households shopped 92339 products)

This table contains all products purchased by household within this study. Each line found in this table is essentially the same line that would be found on a store receipt.

*File: transaction_data2.csv*
```
HOUSEHOLD_KEY -- Uniquely identifies each household

BASKET_ID -- Uniquely identifies a purchase occasion

DAY -- Day when transaction occurred

PRODUCT_ID -- Uniquely identifies each product

QUANTITY -- Number of the products purchased during the trip

SALES_VALUE -- Amount of dollars retailer receives from sale

STORE_ID -- Identifies unique stores

COUPON_MATCH_DISC -- Discount applied due to retailer's match of manufacturer coupon

COUPON_DISC -- Discount applied due to manufacturer coupon

RETAIL_DISC -- Discount applied due to retailer's loyalty card program

TRANS_TIME -- Time of day when transaction occurred

WEEK_NO -- Week of transaction. Ranges 1 -102
```

--------------
##### PRODUCT.csv
(92353 products)

This table contains information on each product sold such as type of product, national or private label and a brand identifier.

*File:product.csv*

```
PRODUCT_ID -- Number that uniquely identifies each product

DEPARTMENT -- Groups similar products together

COMMODITY_DESC -- Groups similar products together at a lower level

SUB_COMMODITY_DESC -- Groups similar products together at a lowest level

MANUFACTURER -- Code that links products with same manufacturer together

BRAND -- Indicates Private or National label brand

CURR_SIZE_OF_PRODUCT -- Indicates package size
```

--------------

##### CASUAL_DATA
(68377 products)

This table signifies whether a given product was featured in the weekly mailer or was part of an in-store display.

*File:causal_data.csv*
```
PRODUCT_ID -- Uniquely identifies each product

STORE_ID -- identifies unique stores

WEEK_NO -- Week of the transaction

DISPLAY -- Display location

MAILER -- Mailer Location
```
--------------
## Code:

```
firstQuestion.py

--
readCSV()- reads transaction_data2.csv
and dumps total sales value of each household, And 4 quarters sales of each household

buildCompleteTopCustomer() -
a) Creates Top Household List by sales value

selectCustomerOverTrend() -
a) Creates moreSpentOverTime, And lessSpentOverTime

```

secondQuestion.py --
readCSV() - Dumps customerMoreQuarterProductDictOverTime,
which has customer's from moreSpentOverTime and product information with 4 quarters. It also dumps productIDCatergoryDict which has categories of products

plotCatergory() -- Plot for Django
plot() -- Plot for Django

thirdQuestion.py --
Input -- lessSpentOverTime, product.csv, transaction_data2.csv
Output -- customerLessQuarterProductDictOverTime.yaml,
productIDCatergoryDict.yaml

thirdApproach.py --
Input -- transaction_data2.csv
Output -- customerSaleDict, customerQuarterSalesDict,
buildTopList() --
output -- topCompleteHouseHoldList.yaml
selectIncreasedTrendCustomer() -- print increased purchase trend
selectDecreasedTrendCustomer() -- prints decreased purchase trend

fourthQuestion.py --

Input -- lessSpentOverTime, hh_demographic.csv
Output --customerDemographicsLessOverTime
This contains demographic details of consumers who purchased less over time

fourthQuestionMore.py --
Input -- moreSpentOverTime.yaml, hh_demographic
Output -- customerDemographicsMoreOverTime.yaml
Demographics of household which purchased more over time

fourthQuestionMarriedUnMarried.py --
List of people from moreSpentOverTime with demographic details (income)
Output -- customerMaritalStatusMoreOverTime.yaml

fourthQuestionAgeGroup.py --
List of people from moreSpentOverTime divided into Age/Income
Output: customerAgeMoreOverTime.yaml

fourthQuestionMoreIncomeHousehold.py --
Details of Household size with Income
Output: customerIncomeMoreOverTime.yaml


fourthQuestionMaritalHouseholdIncome.py --
Details of Household by married/unmarried
Input: moreSpentOverTime.yaml, hh_demographic.csv
Output Details: customerStatusMoreOverTime.yaml
A: 25-34: '1534':75-99K
U: 35-44: '1244':125K

fourthQuestionFullStatusMarried.py --
Input: moreSpentOverTime.yaml, hh_demographic.csv
A:
    45-54:
        'Homeowner' :
                '7' :
                    'KID' = 0
                    'Size' = 2
                    'Income' = 50-74K

Output: customerFullStatusMoreOverTime.yaml

customerAllProductsInEveryQuarter.py --

Three levels of Dictionary

1)Customer Household_ID:
2) Quarter:[0,1,2,3]
3) Product Details
    a) Brand
    b) commodity
    c) Revenue
    d) Sub-commodity

Input -- moreSpentOverTime, product.csv, transaction_data2.csv

Output: customerAllProductsInEveryQuarter.yaml

customerAveragePurchase.py

#Find out the average purchase of Customer
#Average revenue per customer = Customers Total Purchase/Number of Visits
"""
Output:
    CustomerAverageDictionaryPerson.yaml: household_id:'Average Purchase'
    CustomerSaleDictionary.yaml: household_id:'Total Sales'
    customerAverageDictionary.yaml: household_id:'quarter':Average
    Eg:

    customerAverageDictionaryPerson.yaml

    '1': '60.90'
    '100': '89.12'
    '1008': '10.33'
    '1010': '39.71'
    '1011': '42.79'
    '1020': '104.25'

    customerSaleDictionary.yaml

    '1': 1766.0
    '10': 131.0
    '100': 713.0
    '1000': 1717.0
    '1001': 873.0
    '1002': 369.0
    '1003': 1190.0

    customerAverage.yaml
    '1':
  0: 0
  1: 0
  2: 44.0
  3: 146.0
  4: 137.0
  5: 135.0
  6: 526.0
  7: 0
  8: 0
  9: 74.0
  10: 105.0
  11: 599.0
  12: 0


customerEveryQuarterMoreProducts.py --

"""
Output -- for this code
Three levels of Dictionary
12 Quarters.

This script prints out all the values of selected customers in moreOverTime

1)Customer Household_ID:
2) Quarter:[0,1,2,3,4,5,6,7,8,9,10,11]
3) Product Details
    a) Brand
    b) commodity
    c) Revenue
    d) Sub-commodity

Output File: customerEveryQuarterMoreProducts.yaml"
"""

customerLoyal.py --

"""
Build Loyal Customer Dictionary:
    What is Loyal Customer?
    A Customer who has bought continuously in supermarket.
    Where is this data?
    It is in Transaction data.
    How do you find if the customer is Loyal?
    If He purchases Every Week in Year, he is Loyal
    And he has a purchase average of above 50
Output: customerLoyalAverage.yaml

"""

## Release Notes
#### `v1.0.0`

## Contributors
[Rick](https://github.com/ludwigwittgenstein2)
