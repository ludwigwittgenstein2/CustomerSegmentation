#!/usr/bin/env python
from django.shortcuts import render
from graphos.sources.csv_file import CSVDataSource
from graphos.sources.simple import SimpleDataSource
from graphos.renderers.morris import BarChart
import yaml
import sys
import csv

# Global Variable for Dictionary and Product

customerQuarterProductDict = {}
productDict = {}
topCompleteHouseHold = []
moreSpentOverTime = []

def readCSV():
    global customerQuarterProductDict
    global productDict

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/moreSpentOverTime.yaml', 'r' ) as f:
	moreSpentOverTime = yaml.load(f)
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
            
            if row[0] in moreSpentOverTime:
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


    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerMoreQuarterProductDictOverTime.yaml", 'w') as f:
        f.write(yaml.dump(customerQuarterProductDict,default_flow_style=False))
    f.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/productIDCatergoryDict.yaml", 'w' ) as f:
        f.write(yaml.dump(productDict,default_flow_style=False))
    f.close()

def plotCatergory():
    
    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerMoreQuarterProductDictOverTime.yaml", 'r') as f:
        customerQuarterProductDict =  yaml.load(f)
    f.close()
    Quarterly_list = []
    for houseHoldKey, quarterDict in customerQuarterProductDict.items():
        Quarterly_list = [['Category', 'Sale_value']]
        for quarterNo, categoryDict in quarterDict.items():
            for item, saleValue in categoryDict.items():
                Quarterly_list.append([str(quarterNo) +"_" + item, saleValue])
        print houseHoldKey, Quarterly_list

def plot():

    context = {}
    customerQuarterProductDict = {}
    moreOverTime = []

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerMoreQuarterProductDictOverTime.yaml", 'r') as f:
        customerQuarterProductDict =  yaml.load(f)
    f.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/moreSpentOverTime.yaml", 'r') as f:
        moreOverTime =  yaml.load(f)
    f.close()

    Quarterly_list = []
    count = 0

    for houseKey in moreOverTime:
        for houseHoldKey, quarterDict in customerQuarterProductDict.items():
                if houseKey == houseHoldKey:
                    if count  < 10:
                        Quarterly_list = [['Category', 'Sale_value']]
                        for quarterNo, categoryDict in quarterDict.items():
                            for item, saleValue in categoryDict.items():
                                Quarterly_list.append([str(quarterNo) +"_" + item, saleValue])
                        print houseHoldKey,Quarterly_list
                        data = Quarterly_list
                        data_source = SimpleDataSource(data)
                        chart = BarChart(data_source, height=500, width=500, options={'title': 'Quarterly_list'})
                        context['chart'+str(count)] = chart
                        context['house'+str(count)]= houseHoldKey
                        count = count+ 1

def main():
#    readCSV()
#    plotCatergory()
    plot()
if __name__=="__main__":
    main()
