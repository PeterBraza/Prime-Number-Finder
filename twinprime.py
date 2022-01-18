with open("prime.txt", "r") as f:
    score = f.read()
    score_ints = [ int(x) for x in score.split() ]

size = len(score_ints)
for i in range(0, size-1):
    if(score_ints[i] == (score_ints[i+1]-2)):
        print(str(score_ints[i]) + " " + str(score_ints[i+1]) + "\n")
