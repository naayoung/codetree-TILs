m1, d1, m2, d2 = map(int, input().split())
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

if m1 == m2:
    if d2-d1 >= 0:
        answer = day_of_week[d2-d1]
    else:
        answer = day_of_week[7+d2-d1]
else:
    temp = num_of_days[m2]-num_of_days[m1]
    tt = (d2-d1)-(m2-m1)+temp
    if tt >= 0:
        answer = day_of_week[tt]
    else:
        answer = day_of_week[7+tt]
print(answer)