n=int(input())
n=n
for i in range(0,n-1):
    for j in range(0,n):
        if(j==0  or i+j==n-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,n):
    for j in range(0,n):
        if(j==0 or i==j):
            print("*",end="")
        else:
            print(" ",end="")
    print()
