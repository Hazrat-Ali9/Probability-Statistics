# Hazrat Ali
# ID : 221010050
# Batch : 11
# Dept 


def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print("\n")


x = int(input("How Large pattern You Want?\n"))
pattern(x)
