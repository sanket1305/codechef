t = int(input())

for _ in range(t):
    a, b = [int(x) for x in input().split()]
    
    if a>b:
        print("A")
    else:
        print("B")