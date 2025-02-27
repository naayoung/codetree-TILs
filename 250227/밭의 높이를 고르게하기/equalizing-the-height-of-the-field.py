N, H, T = map(int, input().split())
num = list(map(int, input().split()))

# T만큼 자르고 같은 높이 비용구하기
#1. T만큼 자르기
#2. 자른 구간에 최소비용 계산하기

ans = 200
for i in range(0, N-T+1):
    temp_ans = 0
    temp = num[i:i+T]
    for j in temp:
        temp_ans += abs(j-H)
    ans = min(ans, temp_ans)
print(ans)