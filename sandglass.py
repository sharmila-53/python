n=int(input())
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for j in range(0,n-i):
        print("* ",end="")
    print()
for i in range(0,n-1):
    for j in range(0,n-i-2):
        print(" ",end="")
    for j in range(0,i+2):
        print("* ",end="")
    print()
