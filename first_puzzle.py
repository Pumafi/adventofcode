from collections import Counter

def list_distance(list_a, list_b):
    list_a = sorted(list_a)
    list_b = sorted(list_b)

    distance = 0
    for i in range(len(list_a)):
        distance += abs(list_a[i] - list_b[i])

    return distance

def list_similarities(list_a, list_b):
    count_b = Counter(list_b)

    similarity = 0
    for e in list_a:
        similarity += e * count_b[e]

    return similarity


def main():
    # Input parsing
    list_a = []
    list_b = []
    with open("data/input_1.txt") as f:
        for line in f:
            a, b = map(int, line.split("   "))
            list_a.append(a)
            list_b.append(b)

    # First part of puzzle
    print(list_distance(list_a, list_b))

    # Second part
    print(list_similarities(list_a, list_b))

if __name__ == "__main__":
    main()