def trik():
    mapper = ['A', 'B', 'C']
    shift = [[1, 0, 2],
             [0, 2, 1],
             [2, 1, 0]]

    moves = input()
    ball_index = 0
    for move in moves:
        ball_index = shift[ball_index][mapper.index(move)]

    print(ball_index + 1)


trik()
