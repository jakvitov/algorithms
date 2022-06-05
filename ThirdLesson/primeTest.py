#Given a number, test wether it is prime or not

#Better version - we test numbers from 2 to number/2 + 1 - why?
#Numbers bigger than x/2 + 1 cannot be devisors of x, because the smallest multiplication we can make (*2) makes
#them definitely bigger than x. ((x/2)+1)*2=x+2. -> we can save half of the loop
def testPrime(number):
    if number < 1:
        return False;
    for i in range(2, int(number/2) + 1):
        if ((number % i) == 0):
            return False;
    return True;

#We test every possible devisor
def testPrimeNaive(number):
    if number > 1:
        for i in range(2, number):
            if (number % i == 0):
                return False;
        return True;
    else:
        return False;

assert (testPrime(13) == True);
assert (testPrime(5) == True);
assert (testPrime(2) == True);
assert (testPrime(8) == False);
assert (testPrime(123) == False);
assert (testPrime(702613) == True);
assert (testPrime(702611) == False);
assert (testPrime(100000837) == True);
assert (testPrime(-1) == False);