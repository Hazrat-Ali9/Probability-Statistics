# Hazrat Ali
# ID : 221010050
# Batch : 11




import csv

with open('./csv/naive_bayes.csv') as file:
    reader = csv.DictReader(file)
    totalYes = 0
    totalNo = 0
    totalData = 0
    ageData = {}  # {key:[no,yes]}
    incomeData = {}  # {key:[no,yes]}
    creditData = {}  # {key:[no,yes]}
    studentData = {}  # {key:[no,yes]}

    data = []
    tempRes = 'Buys_Computer'


    def insertData(colName, collec):
        if row[colName] in collec.keys():
            if row.get(tempRes) == 'yes':
                collec[row[colName]][1] += 1
            else:
                collec[row[colName]][0] += 1

        else:
            if row.get(tempRes) == 'yes':
                collec[row[colName]] = [0, 1]
            else:
                collec[row[colName]] = [1, 0]


    for row in reader:
        # ===========>COUNT
        totalData += 1
        if row['Buys_Computer'] == 'yes':
            totalYes += 1
        else:
            totalNo += 1

        # ========>AGE
        insertData('Age', ageData)

        # ==============>INCOME
        insertData('Income', incomeData)

        # ==============>CREDIT-RATING
        insertData('Credit_Rating', creditData)

        # ==============>STUDENT
        insertData('Student', studentData)
    # =======>DEBUG
    # print(ageData)
    # print(incomeData)
    # print(creditData)
    # print(studentData)
    # print(totalData)
    # print(totalYes)
    # print(totalNo)

    # =============>USER_INTERACTION
    chooseSituation = {}


    def insertSituation(type, collec):
        f2 = True
        while f2:
            print("There are these variants for ", type, " : ")
            for key in collec.keys():
                print('\t\t', key)
            print("*Input ", type, " : ")
            temp = input()
            if (temp not in collec.keys()):
                print("Invalid Input\n\tTry again!")
                f2 = True
            else:
                chooseSituation[type] = temp
                f2 = False
                print('\n\n\n')


    f1 = True
    while f1:
        print("Now tell me ,what situation you want to predict?")
        print("NOTE: this is a case-sensitive procedure, so be careful!\n \t***So type everything carefully***")
        ready = input("Are you ready?\n\tYES \t NO\n\t")
        if (ready == "YES"):
            insertSituation('Age', ageData)
            insertSituation('Student', studentData)
            insertSituation('Credit_Rating', creditData)
            insertSituation('Income', incomeData)

            yesEvent = totalYes/totalData * studentData[chooseSituation['Student']][1] / totalYes * ageData[chooseSituation['Age']][1] / totalYes * creditData[chooseSituation['Credit_Rating']][1] / totalYes * incomeData[chooseSituation['Income']][1] / totalYes
            noEvent = totalNo/totalData * studentData[chooseSituation['Student']][0] / totalNo * ageData[chooseSituation['Age']][0] / totalNo * creditData[chooseSituation['Credit_Rating']][0] / totalNo * incomeData[chooseSituation['Income']][0] / totalNo
            predictYesPercentage = (yesEvent/(yesEvent+noEvent)) * 100
            predictNoPercentage = (noEvent/(yesEvent+noEvent)) * 100
            print("Prediction Yes = ",predictYesPercentage,'%')
            print("Prediction No =  ",predictNoPercentage,'%')
            if predictYesPercentage > predictNoPercentage:
                print("This customer may be buy a computer.")
            elif predictYesPercentage<predictNoPercentage:
                print("The customer may not buy a computer.")
            else:
                print("There are 50-50 chance that the customer may buy a computer or not.")
            f1 = False
        elif ready == 'NO':
            print("OK, See You Again!")
            f1 = False
        else:
            print("Invalid Input!\n\tLet's try again!")
            f1 = True
    print(chooseSituation)
