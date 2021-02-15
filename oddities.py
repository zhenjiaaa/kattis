def oddities():
    n = int(input())
    judge = ['even', 'odd']

    for _ in range(n):
        i = int(input())
        print(f'{i} is {judge[i%2]}')


oddities()
