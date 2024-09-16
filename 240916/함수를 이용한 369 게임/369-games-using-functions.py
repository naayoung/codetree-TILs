'''
3, 6, 9 중에 하나 들어있거나 숫자 자체가 3의 배수인 경우
'''
#3, 6, 9 중 하나 들어있는 경우
def in_369(i):
    if '3' in str(i):
        return True
    elif '6' in str(i):
        return True
    elif '9' in str(i):
        return True
    return False

#숫자 자체가 3의 배수인 경우
def num_3(i):
    if i%3 == 0:
        return True
    return False

a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if in_369(i) or num_3(i):
        cnt += 1
print(cnt)