import math

inpFile = open("input.txt","r+")
outFile = open("output.txt","w+")

f = inpFile.readlines()
count = 0

def countTwo(n):
    c = 0
    while n % 2 == 0:
        c += 1
        n = n // 2
    return c

t = int(f[count])
twos = 0

for _ in range(t):
    count += 1
    n = int(f[count])
    
    if n == 1:
        # print(0)
        outFile.write("0\n")
    elif n%2!=0:
        # print(1)
        outFile.write("1\n")
    else:
        temp = int(math.sqrt(n))
        if temp*temp == n:
            # print(1)
            outFile.write("1\n")
        else:
            twos = countTwo(n)
            # print("c", twos)
            if twos%2==1:
                # print(-1)
                outFile.write("-1\n")
            else:
                # print(2)
                outFile.write("2\n")