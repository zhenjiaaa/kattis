def kemija08():
    line = input()

    i = 0
    while i < len(line):
        char = line[i]
        if char in ['a', 'e', 'i', 'o', 'u']:
            line = line[:i+1] + line[i+3:]
        i += 1

    print(line)


kemija08()
