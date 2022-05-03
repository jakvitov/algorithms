import math

#Given amount of money, form array representing how much times we need to use amouts on corresponding indexed in the
#"money" array - naive quadratic algorithm
def formAmount(amount):
    if (amount < 0):
        print("Cannot form negative amounts of money!");

    print("Platidlo Počet\tČástka");
    print("-----------------------------");
    money = [500, 200, 100, 50, 20, 10, 5, 2, 1];
    banknotes = [0] * len(money);
    for i in range(0, len(money)):
        if (amount - money[i] >= 0):
            banknotesNumber = math.floor(amount / money[i]);
            minusSize = banknotesNumber * money[i];
            amount -= minusSize;
            print(str("%d Kč\t%d\t%d Kč" % (money[i], banknotesNumber, minusSize)).expandtabs(8));

formAmount(436);
