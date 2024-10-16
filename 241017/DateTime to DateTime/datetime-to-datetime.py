a, b, c = map(int, input().split())

answer = 0
if a <= 11 and b <= 11 and c < 11:
    answer = -1
else:
    answer += (a-11)*24*60
    answer += (b-11)*60
    answer += c-11
print(answer)