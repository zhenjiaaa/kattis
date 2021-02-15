def sifferprodukt(x):
    new_x = 1
    for char in x:
        if char != '0':
            new_x *= int(char)

    if new_x <= 9:
        print(new_x)
    else:
        sifferprodukt(str(new_x))


sifferprodukt(input())
