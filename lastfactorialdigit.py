def lastfactorialdigit():
    t = int(input())

    for _ in range(t):
        n = int(input())
        value = 1
        for i in range(1, n+1):
            value *= i
            value %= 10
        print(value)


lastfactorialdigit()
