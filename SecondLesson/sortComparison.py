#Script to demonstrate efficiency of sorting algos on random generated arrays of data

import random;
import time;

#Given array of ints, sort this array using naive quadratic bubble sort
def bubbleSort(array):
    for i in range(0, len(array)):
        for k in range(i + 1, len(array)):
            if (array[i] > array[k]):
                temp = array[i];
                array[i] = array[k];
                array[k] = temp;

#Given an array and start index I, return index of the next minimal element in the subarray [I - last_element]
def minimal(array, i):
    minIndex = i;
    for k in range(i + 1, len(array)):
        if (array[k] < array[minIndex]):
            minIndex = k;
    return minIndex;

#Given an array, loop trough its elements
def selectSort(array):
    for i in range(0, len(array)):
        lastMin = minimal(array, i);
        #Python syntax for swapping of array elements, in lower level languages done with temporary element
        (array[i], array[lastMin]) = (array[lastMin], array[i]);

#Generate array filled with random values based on the given lenght
def dataGen(size):
    array = [];
    for i in range(0, size):
        array.append(random.randrange(-10000, 10000));
    return array;

#Generate the field of given size and use three different methods to sort it
#Using timestamps print how long it takes each method to sort the array of the given size
#Note that some time will be spent passing the array as a copy, but since the copy times are constant for the same
#arrays, this does not affect the difference between sorting times in this case
def testTime(size):
    array = dataGen(size);
    time1 = time.time();
    selectSort(array.copy());
    time2 = time.time();
    print("Select sort - %s" % (time2 - time1));
    bubbleSort(array.copy());
    time3 = time.time();
    print("Bubble sort - %s" % (time3 - time2));
    array.copy().sort();
    time4 = time.time();
    print("Python sort - %s" % (time4 - time3));

testTime(10000);