# Supermarket
We build a Django prototype in Python to improve revenues with Supermarket data.

Supermarket:

We have dataset from Supermarket, And our goal is to improve Revenues by targeting Segments.

For this project, we use dunnhumby's data for a Supermarket.
___________________________________________________________


About Data-Set:

--------------------------------------------------------------------------------------------------

This dataset contains household level transactions over two years from a group of 2,500 households who are frequent shoppers at a retailer. It contains all of each household’s purchases, not just those from a limited number of categories. For certain households, demographic information as well as direct marketing contact history are included.

Below is the link for whole data-Set:

* [CSV-Files]  (https://www.dropbox.com/sh/6lz05ehkt31x81j/AADxV_STvuCwDujql3VwarGja?dl=0)
* [YAML-FILES](https://www.dropbox.com/sh/lz522q4z2119vh2/AACtNhemZOf4EtCojHccSHBBa?dl=0)

## DATA TABLES:
The following contains the structure of the Dataset, which we used for the whole prototype.

We use (a) to denote a record connected to another table




##### CAMPAIGN_TABLE
(1584 households mailed 30 Campaigns)
```
HOUSEHOLD_KEY
(a)CAMPAIGN_TABLE
   DESCRIPTION
```
##### CAMPAIGN_DESC
(30 Campaigns)
```
(a)CAMPAIGN
DESCRIPTION
START_DAY
END_DAY
```
#####  COUPON_REDEMPT.csv
(434 households redeemed 556 coupons from 30 Campaigns)
```

HOUSEHOLD_KEY
DAY
COUPON_UPC
CAMPAIGN
```

#####  COUPON.csv
(1135 coupons promoted 44133 products for the 30 campaigns)
```
CAMPAIGN
COUPON_UPC
PRODUCT_ID
```
##### HH_DEMOGRAPHIC.csv
```
(801 household)
HOUSEHOLD_KEY
AGE_DESC
MARITAL_STATUS_CODE
INCOME_DESC
HOMEOWNER_DESC
HH_COMP_DESC
HOUSEHOLD_SIZE_DESC
KID_CATEGORY_DESC
```
##### TRANSACTION_DATA.csv
(2500 Households shopped 92339 products)
```
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
```
##### PRODUCT.csv
```
(92353 products)
PRODUCT_ID
COMMODITY_DESC
SUB_COMMODITY_DESC
MANUFACTURER
DEPARTMENT
BRAND
CURR_SIZE_OF_PRODUCT
```
##### CASUAL_DATA.csv
(68377 products)
```
PRODUCT_ID
STORE_ID
WEEK_NO
DISPLAY
MAILER
```
--------------
Code:

firstQuestion.py --
readCSV()- reads transaction_data2.csv and dumps total sales value of each household, And 4 quarters sales of each household

buildCompleteTopCustomer() -
a) Creates Top Household List by sales value

selectCustomerOverTrend() -
a) Creates moreSpentOverTime, And lessSpentOverTime


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
