# N = int(input())

# lst = list(map(int, input().split()))

# # print(lst)
# # [7, 4, 2, 0, 0, 6, 0, 7, 0]
# max_v = 0
# for i in range (N-1):
#     cnt = 0
#     for j in range(i+1, N):
#         if lst[i]>lst[j]:
#             cnt += 1
#     if max_v < cnt:
#         max_v = cnt
# print(max_v)

N = 6
arr = [7, 2, 5, 3, 1, 4]

for i in range(N-1, 0, -1): # for i : N-1 -> 1 정렬한 구간의 마지막 인덱스
    for j in range(i):
        if arr[j] > arr[j+1] : # 오름차순은 큰 수를 오른쪽으로
            arr[j], arr[j+1] = arr[j+1], arr[j] # 자리 맞바꾸기
print(arr)


