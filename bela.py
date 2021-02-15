def bela():
    dom_value = [11, 4, 3, 20, 10, 14, 0, 0]
    non_dom_value = [11, 4, 3, 2, 10, 0, 0, 0]
    mapper = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7']

    n, dom = input().split()
    total = 0
    for _ in range(4 * int(n)):
        card = input()
        value, suit = card[0], card[1]
        if suit == dom:
            total += dom_value[mapper.index(value)]
        else:
            total += non_dom_value[mapper.index(value)]

    return total


print(bela())
