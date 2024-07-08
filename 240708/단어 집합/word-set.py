import sys
input = sys.stdin.readline

while True:
    dic = input().strip()
    answer = []
    if dic == "end":
        break
    else:
        dic_list = list(dic.split())
        for i in dic_list:
            if i in answer:
                continue
            else:
                answer.append(i)
        answer.sort()
        print(*answer)