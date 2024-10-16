m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m1 == m2:
    answer = d2-d1+1
else:
    t1 = num_of_days[m1]-d1+1
    answer = t1+d2

print(answer)