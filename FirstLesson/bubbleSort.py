#Given array of ints, sort this array using naive quadratic bubble sort
def bubbleSort(array):
    for i in range(0, len(array)):
        for k in range(i + 1, len(array)):
            if (array[i] > array[k]):
                temp = array[i];
                array[i] = array[k];
                array[k] = temp;

array = [2, 6, 3, 9, 10, 1, -1];
bubbleSort(array);
print(array);
