# -*- coding: utf-8 -*-
"""Which demographic factors
(e.g.  household size, presence of children, income) appear to affect customer spend?  Engagement with certain categories?
    => HH_DEMOGRAPHIC
Details : HOUSEHOLD_KEY, AGE_DESC[0], MARTIAL_STATUS_CODE[1], INCOME_DESC[2], HOMEOWNER_DESC,HH_COMP_DESC,HOUSEHOLD_SIZE_DESC[5],KID_CATEGORY_DESC[6]
1) Status
2) Age
3) HOMEOWNER_DESC -- Going to Salary
4) Household_key -->
(For each user:KidDiscription’ )
a) Dictionary which is having values KID_CATEGORY_DESC
b) Household Size
c) Income
5)
A:
    45-54:
        'Homeowner' :
                '7' :
                    'KID' = 0
                    'Size' = 2
                    'Income' = 50-74K
b) Segment more/Who are married/un-married. """

import csv
import yaml
import sys

customerFullStatus = {}

def readCSV():
    global customerFullStatus
    with open('/Users/Rick/Desktop/projectFinalFolder/segments/moreSpentOverTime.yaml', 'r' ) as f:
        moreSpentOverTime = yaml.load(f)
    f.close()

    with open("/Users/Rick/Desktop/CSV/hh_demographic.csv", 'r') as f:
        data = csv.reader(f, delimiter=',')
        next(data)
        for row in data:
            if row[7] in moreSpentOverTime:
                if row[1] not in customerFullStatus:
                    customerFullStatus[row[1]] = {}
                    customerFullStatus[row[1]][row[0]] = {}
                    customerFullStatus[row[1]][row[0]][row[3]] = {}
                    customerFullStatus[row[1]][row[0]][row[3]][row[2]] = {}
                    customerFullStatus[row[1]][row[0]][row[3]][row[2]][row[7]]= (row[6],row[5])
                else:
                    if row[0] not in customerFullStatus[row[1]]:
                        customerFullStatus[row[1]][row[0]] = {}
                        customerFullStatus[row[1]][row[0]][row[3]] = {}
                        customerFullStatus[row[1]][row[0]][row[3]][row[2]] = {}
                        customerFullStatus[row[1]][row[0]][row[3]][row[2]][row[7]]= (row[6],row[5])
                    else:
                        if row[3] not in customerFullStatus[row[1]][row[0]]:
                            customerFullStatus[row[1]][row[0]][row[3]] = {}
                            customerFullStatus[row[1]][row[0]][row[3]][row[2]] = {}
                            customerFullStatus[row[1]][row[0]][row[3]][row[2]][row[7]]= (row[6],row[5])
                        else:
                            if row[2] not in customerFullStatus[row[1]][row[0]][row[3]]:
                                customerFullStatus[row[1]][row[0]][row[3]][row[2]] = {}
                                customerFullStatus[row[1]][row[0]][row[3]][row[2]][row[7]]= (row[6],row[5])
                            else:
                                customerFullStatus[row[1]][row[0]][row[3]][row[2]][row[7]]= (row[6],row[5])

        print customerFullStatus
    f.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerFullStatusMoreOverTime.yaml", 'w') as f:
        f.write(yaml.dump(customerFullStatus,default_flow_style=False))
    f.close()

def main():
    readCSV()

if __name__=="__main__":
    main()
