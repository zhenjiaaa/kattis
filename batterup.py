n = int(input())
slugs = 0

for i in map(int, input().split()):
    if i == -1:
        i = 0
        n -= 1
    slugs += i

print(slugs/n)
