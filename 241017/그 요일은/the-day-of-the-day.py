m1, d1, m2, d2 = map(int, input().split())
A = input()

# 요일 배열 (0: Mon, 1: Tue, 2: Wed, 3: Thu, 4: Fri, 5: Sat, 6: Sun)
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 날짜의 총 일수를 계산하는 함수
def num_of_days(m, d):
    total_days = 0
    for i in range(1, m):
        total_days += days_in_month[i]
    total_days += d
    return total_days

# 시작일까지의 총 일수
start_days = num_of_days(m1, d1)
# 2024년 1월 1일은 월요일이므로 요일 인덱스는 0
current_day_index = start_days % 7

# A 요일의 등장 횟수 카운트
count_A = 0

# 날짜 범위 내에서 A 요일의 등장 횟수 계산
for m in range(m1, m2 + 1):
    for d in range(1, days_in_month[m] + 1):
        if m == m1 and d < d1:
            continue  # 시작 날짜 이전의 날짜는 건너뜀
        if m == m2 and d > d2:
            break  # 끝 날짜 이후의 날짜는 건너뜀

        # 현재 요일이 A와 같으면 카운트 증가
        if day_of_week[current_day_index] == A:
            count_A += 1
        
        # 요일 인덱스 업데이트
        current_day_index = (current_day_index + 1) % 7

print(count_A)