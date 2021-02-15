def egypt():
    line = list(map(int, input().split()))

    while line.count(0) != 3:
        line.sort()

        if line[0]**2 + line[1]**2 == line[2]**2:
            print('right')
        else:
            print('wrong')
        line = list(map(int, input().split()))


egypt()
