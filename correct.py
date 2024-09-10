# 정답 코드

N = int(input())
T = 1001

for _ in range(N):
    A, B = map(int, input().split())
    if A <= B:
        T = min(T, B)

if T == 1001:
    print(-1)
else:
    print(T)