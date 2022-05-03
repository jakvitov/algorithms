
#Given a number find all its integer devisors and print them
def findDevison(number):
    numberDevisors = [];
    #Liner solution - loop to the number trying each possibility
    for possibleDevisor in range (2, number):
        if (number % possibleDevisor == 0):
            numberDevisors.append(possibleDevisor);
    print("Číslo: %d -  %a" % (number, numberDevisors));

#Given an array of numbers prints devisors of each of them
def devisors (numbers):
    for i in numbers:
        findDevison(i);


devisors([198, 199, 200]);