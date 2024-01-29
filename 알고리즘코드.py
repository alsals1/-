N = int(input())

lst = list(map(int, input().split()))

# print(lst)
# [7, 4, 2, 0, 0, 6, 0, 7, 0]
max_v = 0
for i in range (N-1):
    cnt = 0
    for j in range(i+1, N):
        if lst[i]>lst[j]:
            cnt += 1
    if max_v < cnt:
        max_v = cnt
print(max_v)