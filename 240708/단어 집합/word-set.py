import sys
input = sys.stdin.readline

answer = []
while True:
    dic = input().strip()
    if dic == "end":
        break
    else:
        dic_list = dic.split()
        for word in dic_list:
            if word not in answer:
                answer.append(word)
        print(*answer)