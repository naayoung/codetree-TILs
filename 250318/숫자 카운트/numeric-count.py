n = int(input())
a, b, c = [], [], []
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

# Please write your code here.
def calc_strike_ball(guess, candidate):
    strike, ball = 0, 0
    for i in range(3):
        if candidate[i] == guess[i]:
            strike += 1
        elif candidate[i] in guess:
            ball += 1
    return strike, ball

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        if j == i:
            continue
        for k in range(1, 10):
            if k == i or k == j:
                continue
            candidate = [i, j, k]
            valid = True
            for nn in range(n):
                guess = list(map(int, str(a[nn])))
                strike, ball = calc_strike_ball(guess, candidate)
                if strike != b[nn] or ball != c[nn]:
                    valid = False
                    break
            if valid:
                ans += 1
print(ans)
