# Hazrat Ali



repeat = True
while repeat:
    size = int(input('Insert size of X or Y :'))
    x = []
    y = []


    def mean(li):
        mean = 0
        for i in li:
            mean += i
        mean /= size
        # print('mean=',mean)
        return mean


    def xyMean(x, y):
        res = 0
        for i in range(size):
            res += (x[i] * y[i])
        res /= size
        # print('xymean',res)
        return res


    def xSqrMean(x):
        res = 0
        for i in x:
            res += (i * i)
        res = res / size
        # print('sqrmean',res)
        return res


    m = 0.00
    c = 0.00


    def calc(givenFlag, x, y):
        global m
        try:
            m = (mean(x) * mean(y) - xyMean(x, y)) / ((mean(x) ** 2) - xSqrMean(x))
        except Exception as e:
            print(e)
            print("Maybe your data set is not properly correct!")
        c = mean(y) - m * mean(x)
        # print(m,'fffffff',c)
        if (givenFlag == 'Y'):
            given = float(input("Insert value of \"X\" : "))
            res = m * given + c
        else:
            given = float(input("Insert value of \"Y\" : "))
            res = (given - c) / m

        print("\n_____________")
        print("Value of 'M': ", "%.2f" % m)
        print("Value of 'C': ", "%.2f" % c)
        print("ANSWER : ", "%.2f" % res)


    for i in range(0, int(size)):
        print(f'Insert {i + 1} number of value of "X" : ')
        x.append(int(input()))

    for i in range(0, int(size)):
        print(f'Insert {i + 1} number of value of "Y" : ')
        y.append(int(input()))

    f1 = True
    while f1:
        question = input("Which value you want to find X or Y?\n \t X : 1 || Y : 2 \n\t")
        match question:
            case '1':
                calc('X', x, y)
                f1 = False
            case '2':
                calc('Y', x, y)
                f1 = False
            case _:
                print('Wrong Input')

    error = True
    while error:
        print("\nAre you want to calculate another Linear Regression?")
        stop = input("YES : 1 \t NO : 2\n")
        match stop:
            case '1':
                repeat = True
                error = False
            case '2':
                repeat = False
                error = False
            case _:
                print("Invalid Input!")
                error = True
