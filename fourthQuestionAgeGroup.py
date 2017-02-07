"""Which demographic factors
(e.g.  household size, presence of children, income) appear to affect customer spend?  Engagement with certain categories?
    => HH_DEMOGRAPHIC
Details : HOUSEHOLD_KEY, AGE_DESC[0], MARTIAL_STATUS_CODE[1], INCOME_DESC[2], HOMEOWNER_DESC,HH_COMP_DESC,HOUSEHOLD_SIZE_DESC[5],KID_CATEGORY_DESC[6]

b) Segment  with Age/Income group eg: 19-24: '1425': 35-94K
                                        25-34: '1242': 35-94K"""


import csv
import yaml
import sys

customerAge = {}


def readCSV():
    global customerAge

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/moreSpentOverTime.yaml', 'r' ) as f:
        moreSpentOverTime = yaml.load(f)
    f.close()

    with open("/Users/Rick/Desktop/CSV/hh_demographic.csv", 'r') as f:
        data = csv.reader(f, delimiter=',')
        next(data)
        for row in data:
            if row[7] in moreSpentOverTime:
                if row[0] not in customerAge:
                    customerAge[row[0]] = {}
                    customerAge[row[0]][row[7]] = row[2]
                else:
                    customerAge[row[0]][row[7]] = row[2]

        print customerAge

    f.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerAgeMoreOverTime.yaml", 'w') as f:
        f.write(yaml.dump(customerAge,default_flow_style=False))
    f.close()



def main():
    readCSV()

if __name__=="__main__":
    main()
