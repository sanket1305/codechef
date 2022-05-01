import math

inpFile = open("input.txt","r+")
outFile = open("output_other.txt","w+")

f = inpFile.readlines()
count = 0

t = int(f[count])

for j in range(t):
    count += 1
    n = int(f[count])
    if(n ==1 ):
        print(0)
        outFile.write("0\n")
        
    elif(n % 2):
        print(1)
        outFile.write("1\n")
        
    else:
        flag = False
        for i in range(2, int(math.floor(math.log(n, 2)) +1)):
            if (math.ceil(pow(n,1/i)) == math.floor(pow(n, 1/i))) and ((math.floor(pow(n, 1/i)) + i) % 2 == 0):
                # print(1)
                outFile.write("1\n")
                flag = True
                break
        
        if(not flag):
            min = 0
            for i in range(1, int(math.ceil(math.log(n, 2))) + 1):
                if(n % (2**i) == 0):
                    min = i
            if(min % 2):
                # print(-1)
                outFile.write("-1\n")
            else:
                # print(2)
                outFile.write("2\n")

    
        