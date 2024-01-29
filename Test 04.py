def solution(maps):
    width = len(maps[0])
    height = len(maps)

    if 2 <= width <= 20 >= height >= 2:
        a = [[None for _ in range(width)] for _ in range(height)]
        b = [[None for _ in range(width)] for _ in range(height)]

        for m in [(0, 0, a), (height-1, width-1, b)]:
            x, y, current_map = m
            current_map[x][y] = 1
            node = [(x, y)]

            while len(node) > 0:
                x, y = node.pop(0)

                for direction in [(1, 0),  (0, 1), (-1, 0), (0, -1)]:
                    next_x, next_y = x + direction[0], y + direction[1]

                    if 0 <= next_x < height and width > next_y >= 0:
                        if current_map[next_x][next_y] is None:
                            current_map[next_x][next_y] = current_map[x][y] + 1

                            if maps[next_x][next_y] == 1:
                                continue
                            node.append((next_x, next_y))

        path_lengths = []
        for x in range(height):
            for y in range(width):
                if a[x][y] and b[x][y]:
                    path_lengths.append(a[x][y] + b[x][y] - 1)

        return min(path_lengths)
