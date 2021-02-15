def planina(n):
    if n == 1:
        return 4
    else:
        return int((2 * planina(n-1)**0.5 - 1)**2)


print(planina(int(input())))
