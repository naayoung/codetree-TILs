m1, d1, m2, d2 = map(int, input().split())
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

if m1 == m2:
    if d2-d1 >= 0 and d2-d1 < 7:
        answer = day_of_week[d2-d1]
    elif d2-d1 >= 7:
        answer = day_of_week[(d2-d1)%7]
    else:
        answer = day_of_week[7+d2-d1]
else:
    temp = (d2-d1)-(m2-m1)+abs(m2-m1)
    
    if temp >= 0 and temp < 7:
        answer = day_of_week[temp]
    elif temp >= 7:
        if m2 == 2:
            answer = day_of_week[temp%7-2]
        else:
            answer = day_of_week[temp%7]
    else:
        answer = day_of_week[7+temp]
print(answer)