
class Stack():
    def __init__(self, initial_configuration):
        initial_configuration = initial_configuration
        self.stack = initial_configuration

    def add(self, crates):
        self.stack = self.stack + crates

    def remove(self, num_of_crates):
        crates = self.stack[-num_of_crates:]
        self.stack = self.stack[:-num_of_crates]
        return crates


    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":
    stacks = [Stack(["0"])]  # Initialize index 0 with empty stack for ease
    with open("initial_config.txt") as config:
        for line in config.readlines():
            initial_stack = line.strip("[]\n").split(",")
            stacks.append(Stack(initial_stack))

    with open("input.txt") as inputs:
        for line in inputs.readlines():
            # move 2 from 4 to 6
            num_of_crates_to_move = int(line.split("from")[0].split("move")[1].strip())
            locations = line.split("from")[1]
            from_location = int(locations.split("to")[0].strip())
            to_location = int(locations.split("to")[1].strip())
            #print(f"moving {num_of_crates_to_move} from {from_location} to {to_location}")
            crates = stacks[from_location].remove(num_of_crates_to_move)
            print(crates)
            stacks[to_location].add(crates)

    i = 0
    final = ""
    for stack in stacks:
        c = stack.remove(1)[0]
        print(f"Stack {i} has crate {c} on top")
        final += c

    print(final)