def simonsays():
    n = int(input())
    for _ in range(n):
        line = input().split()
        if line[:2] == ['Simon', 'says']:
            print(*line[2:])


simonsays()
