import sys
input = sys.stdin.readline

while True:
    dic = input().strip()
    if dic == "end":
        break
    else:
        dic_list = list(dic.split())
        answer = list(set(dic_list))
        answer.sort()
        print(*answer)