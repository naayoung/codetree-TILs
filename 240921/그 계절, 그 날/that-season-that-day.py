#입력값
Y, M, D = map(int, input().split())

def confirm_year(Y):
    # 4의 배수가 아니라면 윤년이 확실히 아닙니다.
    if y % 4 != 0:
        return False
    
    # 여기까지 온 이상 4의 배수임을 가정해도 됩니다.
    # 그 중 100의 배수가 아니라면 확실히 윤년입니다.
    if y % 100 != 0:
        return True
    
    # 여기까지 온 이상 100의 배수임을 가정해도 됩니다.
    # 그 중 400의 배수라면 확실히 윤년입니다.
    if y % 400 == 0:
        return True
    
    # 여기까지 온 이상 100의 배수이지만, 400의 배수가 아닙니다.
    # 따라서 확실히 윤년이 아닙니다.
    return False

#Y해에 M월 D일이 존재하는 지 확인
def sol(Y, M, D):
    if M == 2 and D >= 29:
        if confirm_year(Y) and D == 29:
            return True
        else:
            return False
    if M == 4 or M == 6 or M == 9 or M == 11:
        if D == 31:
            return False
        else:
            return True
    else:
        return True

#계절 확인
def confirm_season(M):
    if M >= 3 and M <= 5:
        season = 'Spring'
    elif M >= 6 and M <= 8:
        season = 'Summer'
    elif M >= 9 and M <= 11:
        season = 'Fall'
    else:
        season = 'Winter'
    return season
#존재한다면, 어떤 계절인지 확인
#존재하지않는다면 -1
if sol(Y, M, D):
    print(confirm_season(M))
else:
    print(-1)