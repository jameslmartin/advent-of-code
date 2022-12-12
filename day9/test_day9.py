from day9 import Position, Grid

def 

def test_tail_unique_positions():
    pos2 = Position(0,1)
    pos3 = Position(0,2)
    pos4 = Position(0,1)
    test_tail = Tail()
    test_tail.visit(pos2)
    test_tail.visit(pos3)
    test_tail.visit(pos4)
    assert test_grid.unique_positions() == 3