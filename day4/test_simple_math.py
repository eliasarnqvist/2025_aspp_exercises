import simple_math

def test_simple_add():
    assert simple_math.simple_add(1,1) == 2
    assert simple_math.simple_add(0,0) == 0
    assert simple_math.simple_add(4,-1) == 3

def test_simple_sub():
    assert simple_math.simple_sub(2,1) == 1
    assert simple_math.simple_sub(1,2) == -1
    assert simple_math.simple_sub(0,0) == 0

def test_simple_mult():
    assert simple_math.simple_mult(2,3) == 6
    assert simple_math.simple_mult(0,4) == 0
    assert simple_math.simple_mult(4,-1) == -4

def test_simple_div():
    assert simple_math.simple_div(4,2) == 2
    assert simple_math.simple_div(0,4) == 0
    assert simple_math.simple_div(4,-1) == -4

def test_poly_first():
    assert simple_math.poly_first(1, 1, 1) == 2
    assert simple_math.poly_first(2, 2, 1) == 4
    assert simple_math.poly_first(3, 1, 2) == 7

def test_poly_second():
    assert simple_math.poly_second(1, 1, 1, 3) == 5
    assert simple_math.poly_second(2, 1, 1, 2) == 11
    assert simple_math.poly_second(3, 1, 1, 2) == 22
