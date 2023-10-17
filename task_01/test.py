import os

os.system("cls")
n = 10
count = 0
number = 2
while count <= 16:
    degree = number**count

    if degree > n:
        break
    print(degree)
    count += 1
