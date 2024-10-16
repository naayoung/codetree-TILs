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

# 시작일의 요일을 계산
start_day_index = (num_of_days(m1, d1) - num_of_days(1, 1)) % 7  # 2024년 1월 1일은 월요일
day_count = 0

# 주어진 범위 내에서 A 요일의 등장 횟수 계산
for i in range(total_days):
    current_day = day_of_week[(start_day_index + i) % 7]
    if current_day == A:
        day_count += 1

print(day_count)