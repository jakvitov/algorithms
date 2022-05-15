#Full implementation of the merge sort algorithm, we use code from the mergeAlgo, which we have created before
#This implementation of merge sort is not the most efficient one, but is better for understanding the basic algorithm
#For better efficiency we would implement merge algorithm on in one array divided just by indexes -> less copying of the array

#Recursively deviding the tree takes us log(n) time (Each time we devide it in half) and composing the two parts together
#is done in linear time -> the overall time is O(n*log(n))
#Warning - do not use this instead of the python .sort() method if possible, this low level programming is slow in python
#and using a library fucntion is more efficient

import math

#A merge algo viz. mergeAlgo.py
def merge(firstArray, secondArray):
    finalArray = [];
    #We until one of the arrays is empty, add the smaller element to the final array and pop him from the list
    while (len(firstArray) > 0 and len(secondArray) > 0):
        if (firstArray[0] <= secondArray[0]):
            finalArray.append(firstArray[0]);
            firstArray.pop(0);
        else:
            finalArray.append(secondArray[0]);
            secondArray.pop(0);

    #Now we append the rest in the larger array, that
    finalArray.extend(firstArray);
    finalArray.extend(secondArray);
    return finalArray;

#Given an array, sort it using a merge sort algo, debugging version with continous merged values printing
#Do not use for actual sorting - the debug printing makes it slow
def mergeSortPrint(array, recursionLevel):
    #While the size of the array is larger that one we call recursively the merge sort on subarrays
    #[0-mid] and [mid+1 - end]
    if (len(array) > 1):
        mid = len(array)//2;

        first = array[:mid];
        second = array[mid:];

        first = mergeSortPrint(first, recursionLevel + 1);
        second = mergeSortPrint(second, recursionLevel + 1);

        print("Merged %a depth - %d" % (merge(first.copy(), second.copy()), recursionLevel));
        return merge(first, second);
    #If the size of the array is 1 -> array of size 1 is already sorted
    return array;


#The actual sort algo without any prints
def mergeSort(array):
    #While the size of the array is larger that one we call recursively the merge sort on subarrays
    #[0-mid] and [mid+1 - end]
    if (len(array) > 1):
        mid = len(array)//2;

        first = array[:mid];
        second = array[mid:];

        first = mergeSort(first);
        second = mergeSort(second);
        #Return the merged arrays - linear time
        return merge(first, second);
    #If the size of the array is 1 -> array of size 1 is already sorted
    return array;


array = [1, -1, 6, 2, 8, -3, 99, -100101];
print(mergeSortPrint(array, 0));