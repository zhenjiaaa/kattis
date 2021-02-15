def oddmanout():
    n = int(input())
    for i in range(n):
        input()
        guest_list = list(map(int, input().split()))
        guest_list.sort()

        while guest_list:
            if len(guest_list) == 1:
                c = guest_list.pop()
            else:
                c = guest_list.pop()
                if c != guest_list[-1]:
                    break
                else:
                    guest_list.pop()

        print(f'Case #{i+1}: {c}')


oddmanout()
