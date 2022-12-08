if __name__ == "__main__":
    contains = 0
    with open("input.txt") as input:
        for line in input.readlines():
            a1, a2 = line.split(",")
            a11, a12 = a1.strip().split("-")
            a21, a22 = a2.strip().split("-")
            a1_range = range(int(a11), int(a12)+1)
            a2_range = range(int(a21), int(a22)+1)
            a1_set = set(a1_range)
            a2_set = set(a2_range)
            print(a1_set.intersection(a2_set))
            if a1_set.intersection(a2_set) != set():
                contains += 1
    print(contains)