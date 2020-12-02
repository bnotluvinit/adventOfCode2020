def get_data():
    f = open("inputs/input2.txt", "r")
    lines = f.read().splitlines()
    f.close()
    return lines


def day2(items):
    x = 0
    y = 0
    for i in items:
        first = int(i.split("-")[0])
        second = int(i.split("-")[1].split(" ")[0])
        character = i.split(" ")[1].split(":")[0]
        password = i.split(" ")[2]
        if first <= password.count(character) <= second:
            x += 1
        if password[first - 1] == character or password[second - 1] == character:
            if not (password[first - 1] == character and password[second - 1] == character):
                y += 1
    return x, y


if __name__ == '__main__':
    answer_1, answer_2 = day2(get_data())
    print("answer 1:", answer_1)
    print("answer 2:", answer_2)
