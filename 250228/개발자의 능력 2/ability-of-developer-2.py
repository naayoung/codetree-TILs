developer = list(map(int, input().split()))

developer.sort()
temp = []
for i in range(3):
    temp.append(developer[i] + developer[-i-1])
print(max(temp)-min(temp))

