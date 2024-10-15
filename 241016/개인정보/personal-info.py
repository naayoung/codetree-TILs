answer = []
for _ in range(5):
    name, h, k = input().split()
    h, k = int(h), float(k)
    answer.append([name, h, k])

answer.sort(key=lambda x:x[0])
print('name')
for a in answer:
    print(*a)
print('')
answer.sort(key=lambda x:(-x[1], x[0]))
print('height')
for a in answer:
    print(*a)