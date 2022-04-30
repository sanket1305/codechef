import random

f = open("input.txt", "w+")

t = 1000
f.write("%d\n" % t)

for i in range(t):

    n = random.randint(1, 10)

    f.write("%d\n" %n)

    for j in range(n):
        temp = random.randint(1,1000)
        if(j == n-1):
            f.write("%d" %temp)
        else:
            f.write("%d " %temp)
    
    f.write("\n")

f.close()
