
#Given amount of money and array representing needed banknotes, print the information in requested format
def printAmount(money, banknotes):

    for i in range(0, len(money)):
        print(str("%d Kč\t%d\t%d Kč" % (money[i], banknotes[i], money[i] * banknotes[i])).expandtabs(8));


#Given amount of money, form array representing how much times we need to use amouts on corresponding indexed in the
#"money" array - naive quadratic algorithm
def formAmount(amount):
    if (amount < 0):
        print("Cannot form negative amounts of money!");
    print("Platidlo Počet\tČástka");
    print("-----------------------------");
    money = [500, 200, 100, 50, 20, 10, 5, 2, 1];
    banknotes = [0] * 9;
    for i in range(0, len(money)):
        while (amount - money[i] >= 0):
            banknotes[i] += 1;
            amount -= money[i];
    printAmount(money, banknotes);


formAmount(436);
