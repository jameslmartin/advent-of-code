import math
import string

letters = string.ascii_letters
numbers = range(1, len(letters)+1)

priority_map = dict(zip(letters, numbers))

class Rucksack():
    
    def __init__(self, contents):
        self.compartment_one = contents[0]
        self.compartment_two = contents[1]
        self.compartment_three = contents[2]

    def overlap(self):
        comp_one = set(self.compartment_one)
        comp_two = set(self.compartment_two)
        comp_three = set(self.compartment_three)
        overlap = comp_one.intersection(comp_two).intersection(comp_three)
        if len(overlap) > 1:
            raise Exception("More than one item overlaps!")
        return list(overlap).pop()

    def priority(self, item):
        return priority_map.get(item)

if __name__ == "__main__":
    priority = 0
    with open("input.txt") as input:
        counter = 1
        group_sack = []
        for line in input.readlines():
            group_sack.append(line.strip())
            if counter == 3:
                ruck = Rucksack(group_sack)
                overlap = ruck.overlap()
                pri = ruck.priority(overlap)
                priority += pri

                counter = 1
                group_sack = []
            else:
                counter += 1

    print(priority)