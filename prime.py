filef = open("prime.txt", "a")
with open("prime.txt", "r") as f:
    score = f.read()
    score_ints = [ int(x) for x in score.split() ]

size = len(score_ints)
large = score_ints[size-1]
counter = 0
for i in range(large, (large * large)):
    counter = 0
    j = 0
    while(score_ints[j] < int(i ** .5) and counter==0):
        if(i%score_ints[j] == 0):
            counter = counter + 1
        j = j + 1

    if(counter == 0):
        filef.write(str(i) + " ")
        print(str(i))
