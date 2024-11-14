import sys
n=int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for i in range(n)]

for i in range(n-1):
    for j in range(n-1):
        if num[j]> num[j+1]:
            temp = num[j]
            num[j]= num[j+1]
            num[j+1]=temp
for i in num:
    print(i)
            