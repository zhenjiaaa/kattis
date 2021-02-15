def sumsquareddigits():
    p = int(input())
    for _ in range(p):
        k, b, n = map(int, input().split())
        list1 = []

        def ssd(base, number, list1):
            coef = number % base
            new_number = (number - coef) // base
            list1.append(coef)
            if new_number != 0:
                ssd(base, new_number, list1)

        ssd(b, n, list1)

        total = sum(list(map(lambda x: x**2, list1)))

        print(f'{k} {total}')


sumsquareddigits()
