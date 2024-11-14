subject = int(input())
scores = list(map(int, input().split()))

map= max(scores)
s=0

for i in range(len(scores)):
    k=scores[i]/map*100
    s = s + k

print(s/len(scores))