
def validate_levels_part_one(levels):
    cur_e = levels[0]

    curr_diff = levels[0] - levels[1]
    cur_sign = curr_diff / abs(curr_diff) if curr_diff != 0 else 0
    safe = True
    for e in levels[1:]:
        diff = cur_e - e
        sign = diff / abs(diff) if diff != 0 else 0
        if abs(diff) > 3 or sign != cur_sign or sign == 0 or cur_sign == 0:
            safe = False
        cur_e = e
        curr_sign = sign
    return safe

def validate_levels(levels):
    # the same as part one but return index for failure
    cur_e = levels[0]

    curr_diff = levels[0] - levels[1]
    cur_sign = curr_diff / abs(curr_diff) if curr_diff != 0 else 0
    safe = True
    for i, e in enumerate(levels[1:]):
        diff = cur_e - e
        sign = diff / abs(diff) if diff != 0 else 0
        if abs(diff) > 3 or sign != cur_sign or sign == 0 or cur_sign == 0:
            return False, i
        cur_e = e
        curr_sign = sign

    return safe, 0

def validate_levels_part_two(levels):
    # actually tried to do it recursively first, it was not pretty, had to start scratch using part 1
    safe, index = validate_levels(levels)
    if not safe:
        safe = False
        if index > 0:
            safe |= validate_levels(levels[:index-1] + levels[index:])[0]
        if index < len(levels) - 1:
            safe |= validate_levels(levels[:index+1] + levels[index+2:])[0]
        safe |= validate_levels(levels[:index] + levels[index+1:])[0]
    return safe


def main():
    # Input parsing

    nb_safe_reports = 0
    with open("data/input_2.txt") as f:
        for line in f:
            levels = list(map(int, line.split(" ")))

            if validate_levels_part_two(levels):
                nb_safe_reports += 1

    print(nb_safe_reports)


if __name__ == "__main__":
    main()