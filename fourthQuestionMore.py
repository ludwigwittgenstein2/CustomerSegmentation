"""Which demographic factors
(e.g.  household size, presence of children, income) appear to affect customer spend?  Engagement with certain categories?
    => HH_DEMOGRAPHIC
Details : HOUSEHOLD_KEY, AGE_DESC[0], MARTIAL_STATUS_CODE[1], INCOME_DESC[2], HOMEOWNER_DESC,HH_COMP_DESC,HOUSEHOLD_SIZE_DESC[5],KID_CATEGORY_DESC[6]

a.) Analyze the details for household key from first question which has less spend over the time, check these column for better understanind of their behaviour
household size, presence of children, income"""


import csv
import yaml
import sys

customerDemographics = {}

def readCSV():
    global customerDemographics

    with open('/Users/Rick/Desktop/projectFinalFolder/segments/moreSpentOverTime.yaml', 'r' ) as f:
        moreSpentOverTime = yaml.load(f)
    f.close()

    with open("/Users/Rick/Desktop/CSV/hh_demographic.csv", 'r') as f:
        data = csv.reader(f, delimiter=',')
        next(data)
        for row in data:
            if row[7] in moreSpentOverTime:
                if row[7] not in customerDemographics:
                    customerDemographics[row[7]] = [row[0],row[1],row[2],row[5],row[6]]
                else:
                    customerDemographics[row[7]] += [row[0],row[1],row[2],row[5],row[6]]
        print customerDemographics

    f.close()

    with open("/Users/Rick/Desktop/projectFinalFolder/segments/customerDemographicsMoreOverTime.yaml", 'w') as f:
        f.write(yaml.dump(customerDemographics,default_flow_style=False))
    f.close()



def main():
    readCSV()

if __name__=="__main__":
    main()
