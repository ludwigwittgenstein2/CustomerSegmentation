#!/usr/bin/env python
import yaml
import sys
import csv
"""
Output -- for this code
Three levels of Dictionary

1)Customer Household_ID:
2) Quarter:[0,1,2,3]
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

    with open('/Users/Rick/Desktop/CSV/transaction_data2.csv', 'rU') as f:
        data = csv.reader(f,delimiter=',')
        next(data)
        for row in data:
            saleValue = (round(float(row[5])))
            if row[0] in moreSpentOverTime:
                if row[0] not in customerQuarterProductDict:
                    customerQuarterProductDict[row[0]] = {}
                    customerQuarterProductDict[row[0]][0] = {}
                    customerQuarterProductDict[row[0]][1] = {}
                    customerQuarterProductDict[row[0]][2] = {}
                    customerQuarterProductDict[row[0]][3] = {}
                    if int(row[9]) >= 0 and int(row[9]) <26:
                        customerQuarterProductDict[row[0]][0][row[3]] = {}
                        customerQuarterProductDict[row[0]][0][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][0][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][0][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][0][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][0][row[3]]["REVENUE"] = saleValue
                    elif int(row[9]) >= 26 and int(row[9]) <51:
                        customerQuarterProductDict[row[0]][1][row[3]] = {}
                        customerQuarterProductDict[row[0]][1][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][1][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][1][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][1][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][1][row[3]]["REVENUE"] = saleValue
                    elif int(row[9]) >=51 and int(row[9]) < 76:
                        customerQuarterProductDict[row[0]][2][row[3]] = {}
                        customerQuarterProductDict[row[0]][2][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][2][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][2][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][2][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][2][row[3]]["REVENUE"] = saleValue
                    else:
                        customerQuarterProductDict[row[0]][3][row[3]] = {}
                        customerQuarterProductDict[row[0]][3][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                        customerQuarterProductDict[row[0]][3][row[3]]["BRAND"] = productDict[row[3]][1]
                        customerQuarterProductDict[row[0]][3][row[3]]["COMMODITY"] = productDict[row[3]][2]
                        customerQuarterProductDict[row[0]][3][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                        customerQuarterProductDict[row[0]][3][row[3]]["REVENUE"] = saleValue
                else:
                    if int(row[9]) >= 0 and int(row[9]) <26:
                        if row[3] not in customerQuarterProductDict[row[0]][0]:
                            customerQuarterProductDict[row[0]][0][row[3]] = {}
                            customerQuarterProductDict[row[0]][0][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][0][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][0][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][0][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][0][row[3]]["REVENUE"] = saleValue
                        else:
                            customerQuarterProductDict[row[0]][0][row[3]]["REVENUE"] += saleValue
                    elif int(row[9]) >= 26 and int(row[9]) <51:
                        if row[3] not in customerQuarterProductDict[row[0]][1]:
                            customerQuarterProductDict[row[0]][1][row[3]] = {}
                            customerQuarterProductDict[row[0]][1][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][1][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][1][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][1][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][1][row[3]]["REVENUE"] = saleValue
                        else:
                            customerQuarterProductDict[row[0]][1][row[3]]["REVENUE"] += saleValue
                    elif int(row[9]) >=51 and int(row[9]) < 76:
                        if row[3] not in customerQuarterProductDict[row[0]][2]:
                            customerQuarterProductDict[row[0]][2][row[3]] = {}
                            customerQuarterProductDict[row[0]][2][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][2][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][2][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][2][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][2][row[3]]["REVENUE"] = saleValue
                        else:
                            customerQuarterProductDict[row[0]][2][row[3]]["REVENUE"] += saleValue
                    else:
                        if row[3] not in customerQuarterProductDict[row[0]][3]:
                            customerQuarterProductDict[row[0]][3][row[3]] = {}
                            customerQuarterProductDict[row[0]][3][row[3]]["DEPARTMENT"] = productDict[row[3]][0]
                            customerQuarterProductDict[row[0]][3][row[3]]["BRAND"] = productDict[row[3]][1]
                            customerQuarterProductDict[row[0]][3][row[3]]["COMMODITY"] = productDict[row[3]][2]
                            customerQuarterProductDict[row[0]][3][row[3]]["SUB-COMMODITY"] = productDict[row[3]][3]
                            customerQuarterProductDict[row[0]][3][row[3]]["REVENUE"] = saleValue
                        else:
                            customerQuarterProductDict[row[0]][3][row[3]]["REVENUE"] += saleValue
    f.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerAllProductsInEveryQuarter.yaml", 'w') as f:
        f.write(yaml.dump(customerQuarterProductDict,default_flow_style=False))
    f.close()


def findQuarterSale():
    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerMoreQuarterAllProduct.yaml","r") as w:
        customerMoreQuarterAllProduct = yaml.load(w)
    w.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/moreSpentOverTime.yaml", 'r') as f:
        moreOverTime =  yaml.load(f)
    f.close()

def main():
    product()

if __name__=="__main__":
    main()
