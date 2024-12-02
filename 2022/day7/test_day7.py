from day7 import is_instruction, parse_instruction

import pytest

@pytest.fixture
def test_input():
    test_input = open("test_input.txt", "r")
    return test_input

def test_is_instruction(test_input):
    line1 = test_input.readline()
    line2 = test_input.readline()
    line3 = test_input.readline()
    is_inst = is_instruction(line1)
    is_inst2 = is_instruction(line2)
    is_inst3 = is_instruction(line3)
    assert is_inst == True
    assert is_inst2 == True
    assert is_inst3 == False

def test_parse_instruction(test_input):
    line1 = test_input.readline()
    inst = parse_instruction(line1)
    inst2 = parse_instruction("$ ls")
    assert inst.name == "cd"
    assert inst.args == "/"
    assert inst2.name == "ls"
    assert inst2.args == None
