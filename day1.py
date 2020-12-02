def get_data():
    f = open("inputs/input1.txt", "r")
    lines = f.read().splitlines()
    f.close()
    int_list = [int(i) for i in lines]
    return int_list


def day1(items):
    for i in range(len(items)):
        sum2020 = 2020 - items[i]
        for j in range(i + 1, len(items)):
            if items[j] == sum2020:
                print items[i] * items[j]


def day2(items):
    for i in range(len(items)):
        for j in range(i, len(items)):
            for k in range(j, len(items)):
                if (items[i] + items[j] + items[k]) == 2020:
                    print(items[i] * items[j] * items[k])


if __name__ == '__main__':
    day1(get_data())
    day2(get_data())
