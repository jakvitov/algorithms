#Merging algorithm is the crucial part of the merge sort algorithm, but also has other usages
#Given two sorted arrays, merge those arrays together into a new sorted array
#Example [1, 4, 55, 100] and [-1, 4, 66] => [-1, 1, 4, 4, 55, 66, 100]
#This is required to be done in linear time O(m+n)

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

firstArray = [0, 1, 2, 5, 8];
secondArray = [-1, 2, 3, 5, 8];

#The arrays are passed as pointers to the array, therefore if we change them in function they change as well,
#if we want to pass them as deep copies (function changes don't affect actual ones), we must add array.copy to the
#function call
print(merge(firstArray.copy(), secondArray.copy()));
print(firstArray);
print(secondArray);
