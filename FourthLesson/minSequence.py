#Given a sequence, find its min, we expect valid inputs - no protection
def findMin():
    min = None;
    occasions = 0;
    inputText = "";
    while (inputText != "0"):
        inputText = input("Zadejte další číslo -> ");
        try:
            inputNum = int(inputText);
        except:
            print("Nezadali jste přirozené číslo!");
            continue;
        if (min == None):
            min = inputNum;
            occasions = 1;
        elif (inputNum < 1):
            continue;
        elif (inputNum < min):
            min = inputNum;
            occasions = 1;
        elif (inputNum == min):
            occasions += 1;
    print("Nejmenší prvek - %d, počet výskytů - %d." %(min, occasions));

findMin();