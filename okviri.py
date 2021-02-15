def okviri():
    row1 = '.'
    row2 = '.'
    row3 = '#'

    line = input()
    for i, char in enumerate(line):
        symbol1, symbol2 = '#', '#'
        if i % 3 == 1:
            symbol2 = '*'
        if i % 3 == 2:
            symbol1, symbol2 = '*', '*'

        row1 += f'.{symbol1}..'
        row2 += f'{symbol1}.{symbol1}.'
        row3 += f'.{char}.{symbol2}'

    # EMERGENCY PATCH TO RESOLVE MISTAKE IN SOME CIRCUMSTANCES WHERE 2, 5, 8 WORDS HAVE * INSTEAD OF #
    if len(line) % 3 == 2:
        row3 = row3[:-1] + '#'

    print(*[row1, row2, row3, row2, row1], sep='\n')


okviri()
