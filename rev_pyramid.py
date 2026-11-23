n = int(input("Enter n: "))

for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end=" ")

    star = 2*i-1

    for k in range(star):
        print("*", end=" ")

    print()


for i in range(n-1, 0, -1):
    for j in range(1, n-i+1):
        print(" ", end=" ")

    star = 2*i-1

    for k in range(star):
        print("*", end=" ")

    print()
    