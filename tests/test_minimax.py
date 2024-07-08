import pytest
from py_version.minimax import minimax

# build_line_inputs = [   
#    ((3,3), (0,0), (0,1), [(0,0), (0,1), (0,2)]),   
#    ((3,3), (0,0), (1,1), [(0,0), (1,1), (2,2)]),   
#    ((3,3,4), (2,2,3), (-1,-1,-1), [(0,0,1), (1,1,2), (2,2,3)]),         
# ]
# @pytest.mark.parametrize("shape,start,diffs,expected", build_line_inputs)
# def test_build_line(shape, start, diffs, expected):
#    returned = n_tac_toe.build_line(shape, start, diffs)
#    assert returned == expected


next_move_inputs = [
    [[[ 1,0,None],[0,None,None],[None,None,None]], (1,1)],
    [[[ 1,0,None],[None,0,None],[None,None,None]], (2,1)],
    [[[ 1,0,0],[None,1,None],[None,None,None]], (2,2)],
]
@pytest.mark.parametrize("state,expected_move", next_move_inputs)
def test_gets_right_next_move(state, expected_move):
    depth = 9
    COMP = +1
    move, _, _ = minimax(state, depth, COMP)
    
    assert move == expected_move
