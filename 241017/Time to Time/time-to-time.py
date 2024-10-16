a, b, c, d = map(int, input().split())

t1 = a*60 + b
t2 = c*60 + d

answer = t2 - t1
print(answer)