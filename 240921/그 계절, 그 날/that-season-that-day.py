#입력값
Y, M, D = map(int, input().split())

def confirm_year(Y):
    #윤년 확인
    if Y%4 == 0:
        if Y%100 == 0 and Y%400 == 0:
            answer = 'True'
        elif Y%100 == 0:
            answer = 'False'
        else:
            answer = 'True'
    else:
        answer = 'False'
    return answer

#Y해에 M월 D일이 존재하는 지 확인
def sol(Y, M, D):
    if M == 2 and D == 29:
        if confirm_year(Y) == 'True':
            return True
        else:
            return False
    if M == 2 or M == 4 or M == 6 or M == 9 or M == 11:
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