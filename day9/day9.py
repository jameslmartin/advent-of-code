class Head():
    def __init__(self, tail):
        self.position = Position(0,0)
        self.tail = tail

    def get_tail(self):
        return self.tail

    def set_tail(self):
        self.tail = tail

    def move(self, new_head_position):
        old_head_position = self.position
        self.position = new_head_position
        head_of_tail, *rest_of_tail = self.tail
        head_of_tail.follow(new_head_position)
        for i, t in enumerate(rest_of_tail):
            new_tail_position = self.tail[i].position
            t.follow(new_tail_position)
            #self.print_snake()

    def print_snake(self):
        print("snake")
        print(f"H: {head.position}")
        for t in self.tail:
            print(t.position)


class Tail():
    def __init__(self, position):
        self.position = position
        self.previous_position = position
        self.visited = [self.position]

    def follow(self, current_head_position):
        self.previous_position = self.position
        new_tail_position_x = self.position.x
        new_tail_position_y = self.position.y
        if not self.is_adjacent_to_head(current_head_position):
            #print(f"is not adjacent! {self.position} not adj to {current_head_position}")
            difference_x = current_head_position.x - self.position.x
            difference_y = current_head_position.y - self.position.y
            if abs(difference_x) > 0 and abs(difference_y) > 0: 
                # diff row and column, move diagonally
                if difference_x > 0:
                    new_tail_position_x = self.position.x + 1
                else:
                    new_tail_position_x = self.position.x - 1
                    
                if difference_y > 0:
                    new_tail_position_y = self.position.y + 1
                else:
                    new_tail_position_y = self.position.y - 1 
            else: 
                # only one is different
                if abs(difference_x) > 1:
                    if difference_x > 0:
                        new_tail_position_x = self.position.x + 1
                    else:
                        new_tail_position_x = self.position.x - 1
                    new_tail_position_y = self.position.y
                else:
                    if difference_y > 0:
                        new_tail_position_y = self.position.y + 1
                    else:
                        new_tail_position_y = self.position.y - 1
                    new_tail_position_x = self.position.x
            
        new_tail_position = Position(new_tail_position_x, new_tail_position_y)
        self.position = new_tail_position
        self.visited.append(self.position)

    def is_adjacent_to_head(self, head_position):
        difference_x = abs(head_position.x - self.position.x)
        difference_y = abs(head_position.y - self.position.y)
        return (
            (difference_x < 2 and difference_y < 2)
        )


class Position():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __key(self):
        return (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.__key())

    def __str__(self):
        return f"({self.x}, {self.y})"


def unique_positions(positions):
    return len(set(positions))


if __name__ == "__main__":
    with open("input.txt") as input:
        
        s = Position(0,0)
        tail = [Tail(s) for _ in range(9)]
        head = Head(tail)

        for line in input.readlines():
            direction, count = line.split(" ")
            current_head_position = head.position
            for move in range(int(count)):
                if direction == "R":
                    # create new head position
                    new_head_position = Position(current_head_position.x+1, current_head_position.y)
                    head.move(new_head_position)
                    current_head_position = new_head_position
                elif direction == "L":
                    new_head_position = Position(current_head_position.x-1, current_head_position.y)
                    head.move(new_head_position)
                    current_head_position = new_head_position
                elif direction == "U":
                    new_head_position = Position(current_head_position.x, current_head_position.y+1)
                    head.move(new_head_position)
                    current_head_position = new_head_position
                elif direction == "D":
                    new_head_position = Position(current_head_position.x, current_head_position.y-1)
                    head.move(new_head_position)
                    current_head_position = new_head_position

            head.print_snake()
            

        tail = head.get_tail()[-1]
        print('visited')
        for v in tail.visited:
            print(v)
        print(unique_positions(tail.visited))
    
