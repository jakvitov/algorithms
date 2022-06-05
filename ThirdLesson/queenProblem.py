#Check if the queens can attack on diagonal
def diagonal(x1, y1, x2, y2):
    if (abs(x1 - x2) == abs(y1 - y2)):
        return True;
    return False;

def dveDamy(x1, y1, x2, y2):
    if (x1 == x2) or (y1 == y2) or diagonal(x1, y1, x2, y2):
        return True;
    return False;

assert (dveDamy(1, 1, 2, 2) == True);
assert (dveDamy(2, 2, 1, 1) == True);
assert (dveDamy(4, 2, 2, 4) == True);
assert (dveDamy(2, 4, 3, 4) == True);
assert (dveDamy(5, 4, 5, 5) == True);
assert (dveDamy(2, 1, 6, 3) == False);
