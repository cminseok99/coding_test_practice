# N = int(input())
# clap = ['3', '6', '9']

# for i in range(1, N+1):
#     count = 0
#     for j in str(i):
#         if j in clap:
#             count += 1
#     if count > 0:
#         i = '-' * count
#     print(i, end=' ')


T = int(input())
for i in range(1, T+1): # 1 ~ 100

    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9')

    if clap == 0:
        print(i, end=' ')
    else:
        print("-" * clap, end=' ')