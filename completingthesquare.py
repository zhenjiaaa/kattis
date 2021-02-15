def euclidian_dist(coord1, coord2):
    x1, y1 = coord1[0], coord1[1]
    x2, y2 = coord2[0], coord2[1]

    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def completingthesquare():
    coord_list = []
    for _ in range(3):
        coord_list.append(tuple(map(int, input().split())))

    origin = (0, 0)
    dist = 0
    for i, j, k in [[0, 1, 2], [1, 0, 2], [2, 0, 1]]:
        if euclidian_dist(coord_list[i], coord_list[j]) == euclidian_dist(coord_list[i], coord_list[k]):
            origin = coord_list[i]
            dist = int(euclidian_dist(coord_list[i], coord_list[j]))

    corner_coordlist = [(origin[0] + dist, origin[1] + dist),
                        (origin[0] + dist, origin[1] - dist),
                        (origin[0] - dist, origin[1] + dist),
                        (origin[0] - dist, origin[1] - dist)]
    print(corner_coordlist)


completingthesquare()
