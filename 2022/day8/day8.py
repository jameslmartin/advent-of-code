class Grid():
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.raw_map = []
        self.tree_map = []

    def add_row_to_raw_map(self, row):
        self.raw_map.append(row)

    def build_tree_map(self):
        for row in range(self.length):
            tree_row = []
            for col in range(self.width):
                t = Tree(self.raw_map[row][col])
                tree_row.append(t)
            self.tree_map.append(tree_row)
        self.set_neighbors()

    def set_neighbors(self):
        for row in range(self.length):
            for col in range(self.width):
                neighbor_up = None if row == 0 else self.tree_map[row-1][col]
                neighbor_down = None if row == len(self.raw_map)-1 else self.tree_map[row+1][col]
                neighbor_left = None if col == 0 else self.tree_map[row][col-1]
                neighbor_right = None if col == len(self.raw_map[0])-1 else self.tree_map[row][col+1]
                t = self.tree_map[row][col]
                t.set_neighbor_up(neighbor_up)
                t.set_neighbor_down(neighbor_down)
                t.set_neighbor_right(neighbor_right)
                t.set_neighbor_left(neighbor_left)

    def print_tree_map(self):
        for row in self.tree_map:
            for col in row:
                print(col, end="")
            print("")

class Tree():
    def __init__(self, height):
        self.height = height
        self.neighbor_up = None
        self.neighbor_down = None
        self.neighbor_left = None
        self.neighbor_right = None

    def set_neighbor_up(self, neighbor):
        self.neighbor_up = neighbor

    def set_neighbor_down(self, neighbor):
        self.neighbor_down = neighbor

    def set_neighbor_left(self, neighbor):
        self.neighbor_left = neighbor

    def set_neighbor_right(self, neighbor):
        self.neighbor_right = neighbor

    def visible_left(self):
        # left neighbor is none or is taller than all neighbors to left
        neighbor_left = self.neighbor_left            
        visible = True

        while neighbor_left is not None:
            if self.height <= neighbor_left.height:
                visible = False
            neighbor_left = neighbor_left.neighbor_left
        return visible

    def visible_right(self):
        neighbor_right = self.neighbor_right
        visible = True
            
        while neighbor_right is not None:
            if self.height <= neighbor_right.height:
                visible = False
            neighbor_right = neighbor_right.neighbor_right
        return visible

    def visible_up(self):
        neighbor_up = self.neighbor_up
        visible = True
        while neighbor_up is not None:
            if self.height <= neighbor_up.height:
                visible = False
            neighbor_up = neighbor_up.neighbor_up
        return visible

    def visible_down(self):
        neighbor_down = self.neighbor_down
        visible = True
        while neighbor_down is not None:
            if self.height <= neighbor_down.height:
                visible = False
            neighbor_down = neighbor_down.neighbor_down
        return visible

    def scenic_score_left(self):
        neighbor_left = self.neighbor_left
        score = 0
        while neighbor_left is not None:
            if self.height > neighbor_left.height:
                score += 1
            else:
                score += 1
                break
            neighbor_left = neighbor_left.neighbor_left
        return score

    def scenic_score_right(self):
        neighbor_right = self.neighbor_right
        score = 0
        while neighbor_right is not None:
            if self.height > neighbor_right.height:
                score += 1
            else:
                score += 1
                break
            neighbor_right = neighbor_right.neighbor_right
        return score

    def scenic_score_up(self):
        neighbor_up = self.neighbor_up
        score = 0
        while neighbor_up is not None:
            if self.height > neighbor_up.height:
                score += 1
            else:
                score += 1
                break
            neighbor_up = neighbor_up.neighbor_up
        return score

    def scenic_score_down(self):
        neighbor_down = self.neighbor_down
        score = 0
        while neighbor_down is not None:
            if self.height > neighbor_down.height:
                score += 1
            else:
                score += 1
                break
            neighbor_down = neighbor_down.neighbor_down
        return score

    def calculate_scenic_score(self):
        scores = [
            self.scenic_score_left(),
            self.scenic_score_right(),
            self.scenic_score_up(),
            self.scenic_score_down()
        ]
        score = 1
        for s in scores:
            score = s * score
        return score

    def __str__(self):
        return str(self.height)

if __name__ == "__main__":
    grid = Grid(0, 0)
    with open("input.txt") as input:
        lines = input.readlines()
        grid = Grid(len(lines), len(lines[0])-1)
        for line in lines: grid.add_row_to_raw_map(line.strip()) 
        grid.build_tree_map()

        visibility_map = []
        scenic_score_map = []
        for row in grid.tree_map:
            vis_row = []
            scenic_score_row = []
            for tree in row:
                vis = 1 if (
                    tree.visible_left() or
                    tree.visible_right() or
                    tree.visible_up() or
                    tree.visible_down()
                ) else 0
                vis_row.append(vis)
                scenic_score_row.append(tree.calculate_scenic_score())
            visibility_map.append(vis_row)
            scenic_score_map.append(scenic_score_row)
        
        max_score = []
        for scores in scenic_score_map:
            max_score.append(max(scores))
        print(max(max_score))