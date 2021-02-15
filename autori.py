def autori():
    name_list = input().split('-')
    print(''.join([name[0] for name in name_list]))


autori()
