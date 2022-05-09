#Scan integers from stdin until the first non integer value comes, return list of scanned values
def scanInput():
    array = [];
    while (1):
        scanned = input();
        try:
            array.append(int(scanned));
        except:
            break;
    return array;

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

#Given two sorted arrays firstArray and secondArray, return a new array containg sorted elements of the first and second
#ones sorted - required linear time
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

#Given an array, return average of the values in the given array
def avg(array):
    if (len(array) == 0):
        return 0;
    sum = 0;
    for i in array:
        sum += i;
    return sum/len(array);

#Return median of the values in the given sorted array, if the array is empty return 0
def median(array):
    if (len(array) == 0):
        return 0;
    mid = int(len(array)/2) - 1;
    return array[mid];

#Main function that takes care about the whole program flow
def main():
    print("Zadejte výšky jednotlivých žáků v 1.A:");
    classA = scanInput();
    print("Zadejte výšky jednotlivých žáků v 1.B:");
    classB = scanInput();
    selectSort(classA);
    selectSort(classB);
    print("Seřazení žáci 1.A: %a" % classA);
    print("Seřazení žáci 1.B: %a" % classB);
    print("Obě třídy sloučené:");
    mergedClasses = merge(classA, classB);
    print(mergedClasses);
    print("Průměr = %d, Median = %d" % (avg(mergedClasses), median(mergedClasses)));

main();