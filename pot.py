n = int(input())
x = 0
for _ in range(n):
    line = input()
    x += int(line[:-1])**int(line[-1])

print(x)
