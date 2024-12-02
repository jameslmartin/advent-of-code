def reduce_cals(current_val, next_val):
    pass

# [1, 2, 3, "", 4, 5, "", 6]
# [5, 9, 6]

if __name__ == "__main__":
    with open("input.txt") as input:
        cals = 0
        inventory = []
        for line in input:
            if line.strip():
                cals += int(line)
            else:
                inventory.append(cals)
                cals = 0

    sorted_inv = sorted(inventory)
    top_three = sorted_inv[-3::]
    print(top_three)
    print(sum(top_three))