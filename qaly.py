n = int(input())
total = float()

for _ in range(n):
    q, y = map(float, input().split())
    total += q * y

print(total)
