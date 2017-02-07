#!/usr/bin/env python
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


"""
import yaml
import sys
import csv

customerQuarterAverageDict = {}
customerSaleDict = {}
customerAverageRevenue = {}

def readCSV():
    global customerSaleDict
    global customerQuarterAverageDict

    with open("/Users/Rick/Desktop/CSV/transaction_data.csv", 'r') as f:
        data = csv.reader(f, delimiter=',')
        next(data)
        for row in data:
            saleValue = (round(float(row[5])))
            if row[0] not in customerSaleDict:
                customerSaleDict[row[0]] = saleValue
            else:
                customerSaleDict[row[0]] += saleValue

            if row[0] not in customerQuarterAverageDict:
                customerQuarterAverageDict[row[0]] = {}
                customerQuarterAverageDict[row[0]][0] = 0
                customerQuarterAverageDict[row[0]][1] = 0
                customerQuarterAverageDict[row[0]][2] = 0
                customerQuarterAverageDict[row[0]][3] = 0
                customerQuarterAverageDict[row[0]][4] = 0
                customerQuarterAverageDict[row[0]][5] = 0
                customerQuarterAverageDict[row[0]][6] = 0
                customerQuarterAverageDict[row[0]][7] = 0
                customerQuarterAverageDict[row[0]][8] = 0
                customerQuarterAverageDict[row[0]][9] = 0
                customerQuarterAverageDict[row[0]][10] = 0
                customerQuarterAverageDict[row[0]][11] = 0

                if int(row[9]) >=0 and int(row[9]) <= 3:
                    customerQuarterAverageDict[row[0]][0] = saleValue
                elif int(row[9]) > 3 and int(row[9]) <= 7:
                    customerQuarterAverageDict[row[0]][1] = saleValue
                elif int(row[9]) > 7 and int(row[9]) <= 11:
                    customerQuarterAverageDict[row[0]][2] = saleValue
                elif int(row[9]) > 12 and int(row[9]) <= 15:
                    customerQuarterAverageDict[row[0]][3] = saleValue
                elif int(row[9]) > 16 and int(row[9]) <= 19:
                    customerQuarterAverageDict[row[0]][4] = saleValue
                elif int(row[9]) > 20 and int(row[9]) <= 23:
                    customerQuarterAverageDict[row[0]][5] = saleValue
                elif int(row[9]) > 24 and int(row[9]) <= 27:
                    customerQuarterAverageDict[row[0]][6] = saleValue
                elif int(row[9]) > 28 and int(row[9]) <= 31:
                    customerQuarterAverageDict[row[0]][7] = saleValue
                elif int(row[9]) > 32 and int(row[9]) <= 35:
                    customerQuarterAverageDict[row[0]][8] = saleValue
                elif int(row[9]) > 36 and int(row[9]) <= 39 :
                    customerQuarterAverageDict[row[0]][9] = saleValue
                elif int(row[9]) > 40 and int(row[9]) <= 43:
                    customerQuarterAverageDict[row[0]][10] = saleValue
                else:
                    customerQuarterAverageDict[row[0]][11] = saleValue
            else:
                if int(row[9]) >=0 and int(row[9]) <= 3:
                    customerQuarterAverageDict[row[0]][0] += saleValue
                elif int(row[9]) > 4 and int(row[9]) <=7:
                    customerQuarterAverageDict[row[0]][1] += saleValue
                elif int(row[9]) > 8 and int(row[9]) <= 11:
                    customerQuarterAverageDict[row[0]][2] += saleValue
                elif int(row[9]) > 12 and int(row[9]) <= 15:
                    customerQuarterAverageDict[row[0]][3] += saleValue
                elif int(row[9]) > 16 and int(row[9]) <= 19:
                    customerQuarterAverageDict[row[0]][4] += saleValue
                elif int(row[9]) > 20 and int(row[9]) <= 23:
                    customerQuarterAverageDict[row[0]][5] += saleValue
                elif int(row[9]) > 24 and int(row[9]) <= 37:
                    customerQuarterAverageDict[row[0]][6] += saleValue
                elif int(row[9]) > 28 and int(row[9]) <= 31:
                    customerQuarterAverageDict[row[0]][7] += saleValue
                elif int(row[9]) > 32 and int(row[9]) <= 35:
                    customerQuarterAverageDict[row[0]][8] += saleValue
                elif int(row[9]) > 36 and int(row[9]) <= 39:
                    customerQuarterAverageDict[row[0]][9] += saleValue
                elif int(row[9]) > 40 and int(row[9]) <= 43:
                    customerQuarterAverageDict[row[0]][10] += saleValue
                else:
                    customerQuarterAverageDict[row[0]][11] += saleValue
    f.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerAverage.yaml", "w") as w:
        w.write(yaml.dump(customerQuarterAverageDict, default_flow_style=False))
    w.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerSaleDictTotal.yaml", "w") as f:
        f.write(yaml.dump(customerSaleDict, default_flow_style=False))
    f.close()

def AverageCSV():
    ''' To find Average, we divide total revenue of person/total visits.'''
    global customerAverageRevenue

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/customerTimesVisit.yaml', "r") as w:
        customerTimesVisit = yaml.load(w)
    w.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerSaleDictTotal.yaml", "r") as w:
        customerSaleDict = yaml.load(w)
    w.close()

    for row,keys in customerTimesVisit.items():
        for new_row, new_keys in customerSaleDict.items():
            if row == new_row and keys != 0:
                customerAverageRevenue[row] = "%0.2f" % (new_keys/keys)

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/customerAverageDictionaryPerson.yaml','w') as w:
        w.write(yaml.dump(customerAverageRevenue,default_flow_style=False))
    w.close()

def main():
    readCSV()
    AverageCSV()

if __name__ == '__main__':
    main()
