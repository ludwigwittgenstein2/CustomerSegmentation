"""Which demographic factors
(e.g.  household size, presence of children, income) appear to affect customer spend?  Engagement with certain categories?
    => HH_DEMOGRAPHIC
Details : HOUSEHOLD_KEY, AGE_DESC[0], MARTIAL_STATUS_CODE[1], INCOME_DESC[2], HOMEOWNER_DESC,HH_COMP_DESC,HOUSEHOLD_SIZE_DESC[5],KID_CATEGORY_DESC[6]

Details of consumer who have more income over time
eg: 100-124K: 2 Adults no Kids"""


import csv
import yaml
import sys

customerIncome = {}


def readCSV():
    global customerIncome

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/moreSpentOverTime.yaml', 'r' ) as f:
        moreSpentOverTime = yaml.load(f)
    f.close()

    with open("/Users/Rick/Desktop/CSV/hh_demographic.csv", 'r') as f:
        data = csv.reader(f, delimiter=',')
        next(data)
        for row in data:
            if row[7] in moreSpentOverTime:
                if row[0] not in customerIncome:
                    customerIncome[row[2]] = {}
                    customerIncome[row[2]][row[7]] = row[4]
                else:
                    customerIncome[row[2]][row[7]] = row[4]

        print customerIncome

    f.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerIncomeMoreOverTime.yaml", 'w') as f:
        f.write(yaml.dump(customerIncome,default_flow_style=False))
    f.close()



def main():
    readCSV()

if __name__=="__main__":
    main()
