def akcija(n):
    # pre: 1 <= n: int <= 100 000
    # post: res = minimal price given the number and cost of books

    total_cost = 0
    price_list = []
    for _ in range(n):
        book_price = int(input())
        total_cost += book_price
        price_list.append(book_price)

    price_list.sort(reverse=True)

    discount = price_list[2::3]
    discount = sum(discount)
    print(total_cost - discount)


akcija(int(input()))
