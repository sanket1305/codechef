import random

f = open("input.txt", "w+")

t = 1000
f.write("%d\n" % t)

for i in range(t):

    n = random.randint(1, 1000)

    f.write("%d\n" %n)

f.close()
