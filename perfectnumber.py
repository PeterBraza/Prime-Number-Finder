sum = 0
for j in range(100000, 1000000):
    sum = 0
    if(j%2==0):
        sum = sum + (j/2)
        third = int(j/3)

        for i in range(1, third + 1):
            if(j%i == 0):
                sum = sum + i
        if(sum == j):
            print(str(j) + " is a perfect number.")
