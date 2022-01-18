import numpy as np
from numpy import log as ln
def factorial(x):
    if(x == 0):
        return 1
    else:
        numenor = 1
        for int in range(1, x):
            numenor *= int
        return numenor
print(str(factorial(1)))
#print(str(np.log(2)))
def li(inp, iter):
    sum = 0
    
    for i in range(0, iter):
        sum = sum + (inp * factorial(i))/((np.log(inp))**(i+1))
    return sum
a = input("What number do you want approximately find primes under?")
b = input("How many iterations do you want?")
expected = li(int(a), int(b))
print("Expected number of primes:" + str(expected))
with open("prime.txt", "r") as f:
    score = f.read()
    score_ints = [ int(x) for x in score.split() ]

ctr = 0
i = 0
while(score_ints[i] < int(a)):
    i = i+1
print("Actual number of primes under " + str(a) + " is " + str(i))
percent_error=((i-expected)/(expected))*100
if(percent_error < 0):
    percent_error = percent_error * -1
print("Percent error is " + str(percent_error)+"%")
