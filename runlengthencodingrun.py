def encoder(line):
    coded_line = []
    i = 1

    char = line[0]
    char_count = 1
    while i < len(line):
        if line[i - 1] == line[i]:
            char_count += 1
            i += 1
        else:
            coded_line.append(char)
            coded_line.append(char_count)

            char = line[i]
            char_count = 1
            i += 1
    coded_line.append(char)
    coded_line.append(char_count)

    print(*coded_line, sep='')


def decoder(line):
    decoded_line = []
    for i in range(0, len(line), 2):
        chars = line[i] * int(line[i+1])
        decoded_line.append(chars)

    print(*decoded_line, sep='')


def runlengthencodingrun():
    EorD, message = input().split()

    if EorD == 'E':
        encoder(message)
    else:
        decoder(message)


runlengthencodingrun()
