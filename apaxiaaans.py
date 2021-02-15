def apaxiaaans():
    line = input()

    new_line = line[0]
    for i in range(1, len(line)):
        if line[i] != line[i - 1]:
            new_line += line[i]

    print(new_line)


apaxiaaans()
