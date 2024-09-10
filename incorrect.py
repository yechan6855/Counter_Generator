# 틀린 코드

import sys
input = sys.stdin.readline
N = int(input().strip())
arr = []
answer = 0

if N == 1:
    A, B = map(int, input().strip().split())
    if B - A >= 0:
        print(B - A + A)
    else:
        print(-1)
else:
    for i in range(N):
        arr.append(list(map(int, input().strip().split())))
    for i in range(N):
        arr[i].append(arr[i][1] - arr[i][0])
    arr.sort(key=lambda x: x[2])
    for i in range(N):
        if arr[i][2] >= 0:
            print(arr[i][2] + arr[i][0])
            answer += 1
            break
    if answer != 1:
        print(-1)