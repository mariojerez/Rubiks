import pytest
from ..RubiksSimulator import Rubiks3

#@pytest.mark.skip(reason="no way of currently testing this")
def test_create_instance_initial_state_correct():
    #arrange
    
    #act
    cube = Rubiks3()
    #assert
    assert cube.white == [['w','w','w'],['w','w','w'],['w','w','w']]
    assert cube.blue == [['b','b','b'],['b','b','b'],['b','b','b']]
    assert cube.green == [['g','g','g'],['g','g','g'],['g','g','g']]
    assert cube.orange == [['o','o','o'],['o','o','o'],['o','o','o']]
    assert cube.yellow == [['y','y','y'],['y','y','y'],['y','y','y']]
    assert cube.red == [['r','r','r'],['r','r','r'],['r','r','r']]

def test_update_orientation_front_blue():
    #arrange
    blue_front_matrix = [['b','b','b'],['b','b','b'],['b','b','b']]
    #act
    cube = Rubiks3()
    cube.updateOrientation("blue")
    #assert
    assert cube.orientation["front"] == blue_front_matrix
