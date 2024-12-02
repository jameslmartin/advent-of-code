class File():
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

class Directory():
    def __init__(self, parent_dir, name):
        self.parent_dir = parent_dir
        self.name = name
        self.child_dirs = []
        self.files = []
        self.over_limit = False
        self.total_space = 0

    def calculate_space(self):
        total_space = sum(list(map(lambda file: file.size, self.files)))
        for child_dir in self.child_dirs:
            total_space += child_dir.calculate_space()
        self.total_space = total_space
        self.over_limit = self.total_space > 100000
        return self.total_space
    
    def add_file(self, file):
        self.files.append(file)

    def add_child_dir(self, child):
        self.child_dirs.append(child)
        self.update_total_space

    def child_dir_exists(self, child):
        return child in list(map(lambda d: d.name, self.child_dirs))

    def get_child_dir(self, child):
        c = None
        for child_dir in self.child_dirs:
            if child_dir.name == child:
                c = child_dir
                break
        return c

class Command():
    def __init__(self, name, args=None):
        self.name = name
        self.args = args

    def __str__(self):
        return f"{self.name} {self.args}"


def is_instruction(input):
    #print(f"input: {input}")
    return input[0] == '$'


def parse_instruction(instruction):
    inst = instruction.strip("\n").split(" ")
    name = inst[1]
    args = None if len(inst) < 3 else inst[2]
    return Command(name, args)

def parse_file(input):
    f = input.strip("\n").split(" ")
    if f[0] == "dir":
        return None
    size = f[0]
    name = f[1]
    return File(name, size)

def walk_for_total(directory, running_total):
    print(f"In dir {directory.name} with {directory.total_space}")
    if not directory.over_limit:
        running_total += directory.total_space
    
    for child in directory.child_dirs:
        running_total = walk_for_total(child, running_total)
    return running_total

def walk_for_smallest(directory, space_needed, smallest):
    if directory.total_space > space_needed and directory.total_space < smallest.total_space:
        smallest = directory
    
    for child in directory.child_dirs:
        smallest = walk_for_smallest(child, space_needed, smallest)
    
    return smallest 

if __name__ == "__main__":
    with open("input.txt") as input:
        root_dir = Directory(None, "/")
        working_dir = root_dir
        line = input.readline()
        listing = False
        while line != "":
            if is_instruction(line):
                listing = False
                instruction = parse_instruction(line)
                if instruction.name == "cd":
                    if instruction.args == "..":
                        working_dir = working_dir.parent_dir
                    elif instruction.args == "/":
                        working_dir = root_dir
                    else:
                        if working_dir.child_dir_exists(instruction.args):
                            working_dir = working_dir.get_child_dir(instruction.args)
                        else:
                            new_dir = Directory(working_dir, instruction.args)
                            working_dir.child_dirs.append(new_dir)
                            working_dir = new_dir
                if instruction.name == "ls":
                    listing = True
            else:
                if listing:
                    listed_file = parse_file(line)
                    if listed_file is not None:
                        working_dir.add_file(listed_file)
            
            line = input.readline()

        root_dir.calculate_space()
        free_space = 70000000 - root_dir.total_space
        needed_space = 30000000
        space_needed_to_install = needed_space - free_space
        print(space_needed_to_install)
        print(root_dir.total_space)
        smallest = walk_for_smallest(root_dir, space_needed_to_install, root_dir)
        print(f"Smallest dir is {smallest.name} with size {smallest.total_space}")
        # dirs_under_limit_total = walk_for_total(root_dir, 0)
        # print(dirs_under_limit_total)