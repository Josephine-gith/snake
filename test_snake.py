from snake import move_snake

def test_move_snake():
    assert move_snake([(10, 15),(11, 15),(12, 15)],(-1,0))==[(9,15),(10,15),(11,15)]

