def absolute(num):
    if (num < 0):
        return - num;
    return num;

#Given two numbers, devise them
def devision(a, b):
    if (b == 0):
        raise "Devision by zero error!";

    origA = a;
    origB = b;

    a = absolute(a);
    b = absolute(b);

    dev = 0;
    while (a >= b):
        dev += 1;
        a -= b;
    
    if (origA > 0 and origB > 0) or (origA < 0 and origB < 0):
        return dev;
    else:
        return - dev;


assert (devision(10, 3) == 3);
assert  (devision(10, -3) == -3);
assert (devision(-6, -2) == 3);
assert (devision(20, 10) == 2);
assert (devision(100, 33) == 3);
assert(devision(-22, 11) == -2);