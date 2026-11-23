

for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end=" ")
    star=2*i-1
    for k in range(star):
        print("*",end=" ")

    print()

