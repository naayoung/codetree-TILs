a = input()
b = input()

while b in a:
    # 가장 앞에 등장하는 B의 시작 위치를 찾기
    index = a.find(b)
    # 찾은 부분을 삭제
    a = a[:index] + a[index+len(b):]

print(a)