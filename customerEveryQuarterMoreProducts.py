#!/usr/bin/env python
import yaml
import sys
import csv
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
"""


# Global Variable for Dictionary and Product

customerQuarterProductDict = {}
productDict = {}
topCompleteHouseHold = []
moreSpentOverTime = []

def product():
    ''' Every product details with quarters.'''
    global customerQuarterProductDict
    global productDict

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/moreSpentOverTime.yaml', 'r' ) as f:
	moreSpentOverTime = yaml.load(f)
    f.close()

    with open("/Users/Rick/Desktop/CSV/product.csv", 'rU') as f:
        data = csv.reader(f, delimiter=',')
        next(data)
        for row in data:
            if row[0] not in productDict:
                productDict[row[0]] = (row[2],row[3],row[4],row[5])
    f.close()
#Create Twelve Quarters by opening transaction_data2 files
#Run through it

    with open('/Users/Rick/Desktop/CSV/transaction_data2.csv', 'rU') as f:
        data = csv.reader(f,delimiter=',')
        next(data)
        for row in data:
            saleValue = (round(float(row[5])))
            quantity = (round(float(row[4])))
            if row[0] in moreSpentOverTime:
                if row[0] not in customerQuarterProductDict:
                    customerQuarterProductDict[row[0]] = {}
                    customerQuarterProductDict[row[0]][0] = {}
                    customerQuarterProductDict[row[0]][1] = {}
                    customerQuarterProductDict[row[0]][2] = {}
                    customerQuarterProductDict[row[0]][3] = {}
                    customerQuarterProductDict[row[0]][2] = {}
                    customerQuarterProductDict[row[0]][3] = {}
                    customerQuarterProductDict[row[0]][4] = {}
                    customerQuarterProductDict[row[0]][5] = {}
                    customerQuarterProductDict[row[0]][6] = {}
                    customerQuarterProductDict[row[0]][7] = {}
                    customerQuarterProductDict[row[0]][8] = {}
                    customerQuarterProductDict[row[0]][9] = {}
                    customerQuarterProductDict[row[0]][10] = {}
                    customerQuarterProductDict[row[0]][11] = {}

                    if int(row[9]) >= 0 and int(row[9]) <=3:
                        customerQuarterProductDict[row[0]][0][row[3]] = {}
                        customerQuarterProductDict[row[0]][0][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][0][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][0][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][0][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][0][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][0][row[3]]["QUANTITY"] = quantity
                    elif int(row[9]) >3 and int(row[9]) <=7:
                        customerQuarterProductDict[row[0]][1][row[3]] = {}
                        customerQuarterProductDict[row[0]][1][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][1][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][1][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][1][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][1][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][1][row[3]]["QUANTITY"] = quantity
                    elif int(row[9]) >7 and int(row[9]) <=11 :
                        customerQuarterProductDict[row[0]][2][row[3]] = {}
                        customerQuarterProductDict[row[0]][2][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][2][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][2][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][2][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][2][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][2][row[3]]["QUANTITY"] = quantity
                    elif int(row[9]) >11 and int(row[9]) <=15:
                        customerQuarterProductDict[row[0]][3][row[3]] = {}
                        customerQuarterProductDict[row[0]][3][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][3][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][3][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][3][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][3][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][3][row[3]]["QUANTITY"] = quantity
                    elif int(row[9]) > 15 and int(row[9]) <= 19:
                        customerQuarterProductDict[row[0]][4][row[3]] = {}
                        customerQuarterProductDict[row[0]][4][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][4][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][4][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][4][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][4][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][4][row[3]]["QUANTITY"] = quantity
                    elif int(row[9]) > 19 and int(row[9]) <=23 :
                        customerQuarterProductDict[row[0]][5][row[3]] = {}
                        customerQuarterProductDict[row[0]][5][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][5][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][5][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][5][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][5][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][5][row[3]]["QUANTITY"] = quantity
                    elif int(row[9]) > 23 and int(row[9]) <=27:
                        customerQuarterProductDict[row[0]][6][row[3]] = {}
                        customerQuarterProductDict[row[0]][6][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][6][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][6][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][6][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][6][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][6][row[3]]["QUANTITY"] = quantity
                    elif int(row[9]) > 27 and int(row[9]) <= 31:
                        customerQuarterProductDict[row[0]][7][row[3]] = {}
                        customerQuarterProductDict[row[0]][7][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][7][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][7][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][7][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][7][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][7][row[3]]["QUANTITY"] = quantity
                    elif int(row[9]) > 31 and int(row[9]) <= 35 :
                        customerQuarterProductDict[row[0]][8][row[3]] = {}
                        customerQuarterProductDict[row[0]][8][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][8][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][8][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][8][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][8][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][8][row[3]]["QUANTITY"] = quantity
                    elif int(row[9]) >35 and int(row[9]) <39:
                        customerQuarterProductDict[row[0]][9][row[3]] = {}
                        customerQuarterProductDict[row[0]][9][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][9][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][9][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][9][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][9][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][9][row[3]]["QUANTITY"] = quantity
                    elif int(row[9]) >39 and int(row[9]) < 43:
                        customerQuarterProductDict[row[0]][10][row[3]] = {}
                        customerQuarterProductDict[row[0]][10][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][10][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][10][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][10][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][10][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][10][row[3]]["QUANTITY"] = quantity
                    else:
                        customerQuarterProductDict[row[0]][11][row[3]] = {}
                        customerQuarterProductDict[row[0]][11][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][11][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][11][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][11][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][11][row[3]]["REVENUE"] = saleValue
                        customerQuarterProductDict[row[0]][11][row[3]]["QUANTITY"] = quantity
                else:
                    if int(row[9]) >= 0 and int(row[9]) <=3:
                        if row[3] not in customerQuarterProductDict[row[0]][0]:
                            customerQuarterProductDict[row[0]][0][row[3]] = {}
                            customerQuarterProductDict[row[0]][0][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][0][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][0][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][0][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][0][row[3]]["REVENUE"] = saleValue
                            customerQuarterProductDict[row[0]][0][row[3]]["QUANTITY"] = quantity
                        else:
                            customerQuarterProductDict[row[0]][0][row[3]]["REVENUE"] += saleValue

                    elif int(row[9]) >3 and int(row[9]) <=7:
                        if row[3] not in customerQuarterProductDict[row[0]][1]:
                            customerQuarterProductDict[row[0]][1][row[3]] = {}
                            customerQuarterProductDict[row[0]][1][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][1][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][1][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][1][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][1][row[3]]["REVENUE"] = saleValue
                            customerQuarterProductDict[row[0]][1][row[3]]["QUANTITY"] = quantity
                        else:
                            customerQuarterProductDict[row[0]][1][row[3]]["REVENUE"] += saleValue

                    elif int(row[9]) >7 and int(row[9]) <=11 :
                        if row[3] not in customerQuarterProductDict[row[0]][2]:
                            customerQuarterProductDict[row[0]][2][row[3]] = {}
                            customerQuarterProductDict[row[0]][2][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][2][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][2][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][2][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][2][row[3]]["REVENUE"] = saleValue
                            customerQuarterProductDict[row[0]][2][row[3]]["QUANTITY"] = quantity
                        else:
                            customerQuarterProductDict[row[0]][2][row[3]]["REVENUE"] += saleValue

                    elif int(row[9]) >11 and int(row[9]) <=15:
                        if row[3] not in customerQuarterProductDict[row[0]][3]:

                            customerQuarterProductDict[row[0]][3][row[3]] = {}
                            customerQuarterProductDict[row[0]][3][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][3][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][3][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][3][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][3][row[3]]["REVENUE"] = saleValue
                            customerQuarterProductDict[row[0]][3][row[3]]["QUANTITY"] = quantity
                        else:
                            customerQuarterProductDict[row[0]][3][row[3]]["REVENUE"] += saleValue

                    elif int(row[9]) > 15 and int(row[9]) <= 19:
                            if row[3] not in customerQuarterProductDict[row[0]][4]:

                                customerQuarterProductDict[row[0]][4][row[3]] = {}
                                customerQuarterProductDict[row[0]][4][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                                customerQuarterProductDict[row[0]][4][row[3]]["BRAND"] = productDict[row[3]][1]
                                customerQuarterProductDict[row[0]][4][row[3]]["COMMODITY"] = productDict[row[3]][2]
                                customerQuarterProductDict[row[0]][4][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                                customerQuarterProductDict[row[0]][4][row[3]]["REVENUE"] = saleValue
                                customerQuarterProductDict[row[0]][4][row[3]]["QUANTITY"] = quantity
                            else:
                                customerQuarterProductDict[row[0]][4][row[3]]["REVENUE"] += saleValue

                    elif int(row[9]) > 19 and int(row[9]) <=23:
                        if row[3] not in customerQuarterProductDict[row[0]][5]:
                            customerQuarterProductDict[row[0]][5][row[3]] = {}
                            customerQuarterProductDict[row[0]][5][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][5][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][5][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][5][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][5][row[3]]["REVENUE"] = saleValue
                            customerQuarterProductDict[row[0]][5][row[3]]["QUANTITY"] = quantity
                        else:
                            customerQuarterProductDict[row[0]][5][row[3]]["REVENUE"] += saleValue

                    elif int(row[9]) > 23 and int(row[9]) <=27:
                        if row[3] not in customerQuarterProductDict[row[0]][6]:

                            customerQuarterProductDict[row[0]][6][row[3]] = {}
                            customerQuarterProductDict[row[0]][6][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][6][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][6][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][6][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][6][row[3]]["REVENUE"] = saleValue
                            customerQuarterProductDict[row[0]][6][row[3]]["QUANTITY"] = quantity
                        else:
                            customerQuarterProductDict[row[0]][6][row[3]]["REVENUE"] += saleValue


                    elif int(row[9]) > 27 and int(row[9]) <= 31:
                        if row[3] not in customerQuarterProductDict[row[0]][7]:
                            customerQuarterProductDict[row[0]][7][row[3]] = {}
                            customerQuarterProductDict[row[0]][7][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][7][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][7][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][7][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][7][row[3]]["REVENUE"] = saleValue
                            customerQuarterProductDict[row[0]][7][row[3]]["QUANTITY"] = quantity
                        else:
                            customerQuarterProductDict[row[0]][7][row[3]]["REVENUE"] += saleValue

                    elif int(row[9]) > 31 and int(row[9]) <= 35 :
                        if row[3] not in customerQuarterProductDict[row[0]][8]:
                            customerQuarterProductDict[row[0]][8][row[3]] = {}
                            customerQuarterProductDict[row[0]][8][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][8][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][8][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][8][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][8][row[3]]["REVENUE"] = saleValue
                            customerQuarterProductDict[row[0]][8][row[3]]["QUANTITY"] = quantity
                        else:
                            customerQuarterProductDict[row[0]][8][row[3]]["REVENUE"] += saleValue

                    elif int(row[9]) >35 and int(row[9]) <=39:
                        if row[3] not in customerQuarterProductDict[row[0]][9]:
                            customerQuarterProductDict[row[0]][9][row[3]] = {}
                            customerQuarterProductDict[row[0]][9][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][9][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][9][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][9][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][9][row[3]]["REVENUE"] = saleValue
                            customerQuarterProductDict[row[0]][9][row[3]]["QUANTITY"] = quantity
                        else:
                            customerQuarterProductDict[row[0]][9][row[3]]["REVENUE"] += saleValue

                    elif int(row[9]) >39 and int(row[9]) < 43:
                        if row[3] not in customerQuarterProductDict[row[0]][10]:
                            customerQuarterProductDict[row[0]][10][row[3]] = {}
                            customerQuarterProductDict[row[0]][10][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][10][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][10][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][10][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][10][row[3]]["REVENUE"] = saleValue
                            customerQuarterProductDict[row[0]][10][row[3]]["QUANTITY"] = quantity
                        else:
                            customerQuarterProductDict[row[0]][10][row[3]]["REVENUE"] += saleValue
                    else:
                        if row[3] not in customerQuarterProductDict[row[0]][11]:
                            customerQuarterProductDict[row[0]][11][row[3]] = {}
                            customerQuarterProductDict[row[0]][11][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][11][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][11][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][11][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][11][row[3]]["REVENUE"] = saleValue
                            customerQuarterProductDict[row[0]][11][row[3]]["QUANTITY"] = quantity
                        else:
                            customerQuarterProductDict[row[0]][11][row[3]]["REVENUE"] += saleValue
    f.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerEveryQuarterMoreProducts.yaml", 'w') as f:
        f.write(yaml.dump(customerQuarterProductDict,default_flow_style=False))
    f.close()


def main():
    product()

if __name__=="__main__":
    main()
