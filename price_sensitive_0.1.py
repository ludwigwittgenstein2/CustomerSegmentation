#!/bin/python

"""
Objective: To find Price Sensitive consumers

How: i) Find out coupon redeemed by top 20 consumers
    ii) Find out Product Details by top 20 Consumers


Code:
Function--coupon(): (What it does?)
  i) Read Coupon redemp csv files
  ii) Divides Days into Quarters
  ii) Creates a dictionary with
 Output:couponRedemptDict[housholdkey][quarter] = (Campaign, COUPON_UPC)

findConsumer()
 Objective: Find the people in top20 who redeemed

What's happening inside?
    i) Opening moreSpentOverTime
    ii) Opening coupon_redem.csv
    iii) In Both, we find the people who have redeemed
    iv) Storing it in Consumer_coupon_redemp.yaml

productDetails()
Objective: Find the details of the products redeemed by people
    i) Open TopConsumers
    ii) Open

"""

moreSpentOverTime = []
findConsumerDict = {}
consumerList = []
couponDict = {}
couponCamp = {}
quarter = 0
product = {}
household_id_dict = {}
coupon_details = {}

import csv
import yaml

def coupon():
    global couponRedemption
    global quarter
    global couponDict

    with open('/Users/Rick/Desktop/CSV/coupon_redempt.csv', 'r') as w:
        couponRedemption = csv.reader(w, delimiter = ',')
        next(couponRedemption)

        for row in couponRedemption:
            if int(row[1]) > 21:
                quarter = 1
            if int(row[1]) > 49:
                quarter = 2
            if int(row[1]) > 77:
                quarter = 3
            if int(row[1]) > 105:
                quarter = 4
            if int(row[1]) > 133:
                quarter = 5
            if int(row[1]) > 161:
                quarter = 6
            if int(row[1]) > 189:
                quarter = 7
            if int(row[1]) > 217:
                quarter = 8
            if int(row[1]) > 245:
                quarter = 9
            if int(row[1]) > 273:
                quarter = 10
            if int(row[1]) > 301:
                quarter = 11
            else:
                quarter = 12

            if row[0] not in couponDict:
                couponDict[row[0]] = {}
                couponDict[row[0]][quarter] = {}
            else:
                if quarter not in couponDict[row[0]]:
        # Campaign[row[3], coupon_upc[row[2]]
                    couponDict[row[0]][quarter] = (row[3], row[2])
                else:
                    couponDict[row[0]][quarter] = (row[3], row[2])
        w.close()
    print couponDict

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/couponDictionary.yaml", "w") as w:
        w.write(yaml.dump(couponDict, default_flow_style= False))
    w.close()

def findConsumer():
    """Find the consumers who redeemed from top 20"""
    global findConsumerDict
    global consumerList
    global household_id_dict

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/moreSpentOverTime.yaml', 'r') as w:
        moreSpentOverTime = yaml.load(w)
    w.close()

    with open('/Users/Rick/Desktop/CSV/coupon_redempt.csv', 'rb') as w:
        couponData = csv.reader(w, delimiter = ',')
        next(couponData)

        for row in couponData:
            if row[0] in moreSpentOverTime:
                if row[0] not in household_id_dict:
                    household_id_dict[row[0]] = [row[2]]

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/Consumer_coupon_redemp.yaml', 'w') as w:
        w.write(yaml.dump(household_id_dict, default_flow_style=False))
    w.close()

def couponDetails():
    """Coupon Details gives us the Product_ID
        TopConsumerCoupon = '1': '2154235'
                            Household_id, 'Coupon_upc'

        coupon.csv -- 'coupon_upc', 'product_id', 'campaign'
        dictionary created: coupon_details ->coupon_upc= product_id
    """
    coupon_details = {}
    coupon_upc_top = []

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/Consumer_coupon_redemp.yaml', 'r') as w:
        TopConsumerCoupon = yaml.load(w)
    w.close()

    with open('/Users/Rick/Desktop/CSV/coupon.csv', 'rb') as w:
        couponDetails = csv.reader(w, delimiter = ',')

        for row in couponDetails:
            for first, second in TopConsumerCoupon.items():
                if second[0] == row[0]:
                    coupon_upc = second[0]
                    coupon_details[coupon_upc] = row[1]
    w.close()

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/couponUPC_ProductID.yaml', 'w') as w:
        w.write(yaml.dump(coupon_details,default_flow_style=False))
    w.close()

def productDetails():
    """Product Details of coupons redeemed"""
    product_id = {}

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/couponUPC_ProductID.yaml', 'r') as r:
        coupon_product = yaml.load(r)
    r.close()

    with open('/Users/Rick/Desktop/CSV/product.csv', 'rU') as w:
        product = csv.reader(w, delimiter = ',')
        for row in product:
            for first, second in coupon_product.items():
                if second == row[0]:
                    product_id[first] = row
    w.close()

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/productDetails_couponsRedeemed.yaml', 'w') as w:
        w.write(yaml.dump(product_id, default_flow_style=False))
    w.close()

def main():
#   coupon()
#   findConsumer()
#   couponDetails()
    productDetails()

if __name__ == '__main__':
    main()



