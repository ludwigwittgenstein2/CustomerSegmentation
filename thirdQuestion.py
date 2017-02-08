#thirdQuestion

import yaml
import sys
import csv

customerQuarterProductDict={}
productDict = {}
topCompleteHouseHold = []
lessSpentOverTime = []

def readCSV():
    global customerQuarterProductDict
    global productDict

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/lessSpentOverTime.yaml', 'r') as f:
        lessSpentOverTime = yaml.load(f)
        f.close()

    with open("/Users/Rick/Desktop/CSV/product.csv", 'r') as f:
        data = csv.reader(f, delimiter=',')
        next(data)
        for row in data:
            if row[0] not in productDict:
                productDict[row[0]] = row[2]
    f.close()

    with open("/Users/Rick/Desktop/CSV/transaction_data2.csv", 'r') as f:
        data = csv.reader(f, delimiter=',')
        next(data)
        for row in data:
            saleValue = (round(float(row[5])))

            if row[0] in lessSpentOverTime:
                if row[0] not in customerQuarterProductDict:
                    customerQuarterProductDict[row[0]] = {}
                    customerQuarterProductDict[row[0]][0] = {}
                    customerQuarterProductDict[row[0]][1] = {}
                    customerQuarterProductDict[row[0]][2] = {}
                    customerQuarterProductDict[row[0]][3] = {}
                    if int(row[9]) >= 0 and int(row[9]) <26:
                        customerQuarterProductDict[row[0]][0][productDict[row[3]]] = saleValue
                    elif int(row[9]) >= 26 and int(row[9]) <51:
                        customerQuarterProductDict[row[0]][1][productDict[row[3]]] = saleValue
                    elif int(row[9]) >=51 and int(row[9]) < 76:
                        customerQuarterProductDict[row[0]][2][productDict[row[3]]] = saleValue
                    else:
                        customerQuarterProductDict[row[0]][3][productDict[row[3]]] = saleValue
                else:
                    if int(row[9]) >= 0 and int(row[9]) <26:
                        if productDict[row[3]] not in customerQuarterProductDict[row[0]][0] :
                            customerQuarterProductDict[row[0]][0][productDict[row[3]]] = saleValue
                        else:
                            customerQuarterProductDict[row[0]][0][productDict[row[3]]] += saleValue
                    elif int(row[9]) >= 26 and int(row[9]) <51:
                        if productDict[row[3]] not in customerQuarterProductDict[row[0]][1] :
                            customerQuarterProductDict[row[0]][1][productDict[row[3]]] = saleValue
                        else:
                            customerQuarterProductDict[row[0]][1][productDict[row[3]]] += saleValue
                        customerQuarterProductDict[row[0]][1][productDict[row[3]]] += saleValue
                    elif int(row[9]) >=51 and int(row[9]) < 76:
                        if productDict[row[3]] not in customerQuarterProductDict[row[0]][2] :
                            customerQuarterProductDict[row[0]][2][productDict[row[3]]] = saleValue
                        else:
                            customerQuarterProductDict[row[0]][2][productDict[row[3]]] += saleValue
                        customerQuarterProductDict[row[0]][2][productDict[row[3]]] += saleValue
                    else:
                        if productDict[row[3]] not in customerQuarterProductDict[row[0]][3] :
                            customerQuarterProductDict[row[0]][3][productDict[row[3]]] = saleValue
                        else:
                            customerQuarterProductDict[row[0]][3][productDict[row[3]]] += saleValue
    f.close()


    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerLessQuarterProductDictOverTime.yaml", 'w') as f:
        f.write(yaml.dump(customerQuarterProductDict,default_flow_style=False))
    f.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/productIDCatergoryDict.yaml", 'w' ) as f:
        f.write(yaml.dump(productDict,default_flow_style=False))
    f.close()


def main():
    readCSV()

if __name__=="__main__":
    main()
