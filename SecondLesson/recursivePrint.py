#User recursive function call to print array
def recursiePrint(array, i):
    if (i == len(array)):
        return;
    else:
        print(array[i]);
        recursiePrint(array, i + 1);

array = [-1, 2, 1, 4, 5, -10];
recursiePrint(array, 0);