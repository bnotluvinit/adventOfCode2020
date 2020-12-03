def get_data():
    f = open("inputs/input3.txt", "r")
    mini_map = [line for line in f]
    f.close()
    return mini_map


def part_1(mini_map):
    trees = 0
    width = len(mini_map[0]) - 1
    position = [0, 0]
    slope = [1, 3]

    while position[0] < len(mini_map):
        if mini_map[position[0]][position[1]] == '#':
            trees += 1
        position[0] += slope[0]
        position[1] += slope[1]
        position[1] = position[1] % width

    print trees


def part_2(mini_map):
    width = len(mini_map[0]) - 1
    slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]

    result = 1

    for slope in slopes:
        trees = 0
        position = [0, 0]
        while position[0] < len(mini_map):
            if mini_map[position[0]][position[1]] == "#":
                trees += 1
            position[0] += slope[0]
            position[1] += slope[1]
            position[1] = position[1] % width
        result *= trees

    print result


if __name__ == '__main__':
    part_1(get_data())
    part_2(get_data())
