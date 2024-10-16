m1, d1, m2, d2 = map(int, input().split())
A = input()

day_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def num_of_days(m, d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0

    for i in range(1, m):
        total_days += days[i]
        
    total_days += d
    
    return total_days    

total_days = num_of_days(m2, d2) - num_of_days(m1, d1) + 1

if day_of_week[total_days%7] == A:
    answer = total_days//7+1
else:
    if total_days//7 == 0:
        answer = 1
    else:
        answer = total_days//7

print(answer)