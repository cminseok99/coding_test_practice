N = int(input())
S = 0
C = N
t = 0
i = 0
while True:
    t = N//10 + N%10
    S = (N%10)*10 + t%10
    i = i+1
    N = S
    if S == C:
        break
print(i)