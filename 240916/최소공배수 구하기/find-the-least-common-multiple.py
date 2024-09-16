import math

def lcm(n, m):
    temp = math.gcd(n, m)
    print(temp * (n//temp) * (m//temp))

n, m = map(int, input().split())
lcm(n, m)