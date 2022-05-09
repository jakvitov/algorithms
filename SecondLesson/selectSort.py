#A quadratic sort algorithm, quite similiar to bubble sort - n^2 but the multiplicative constant is smaller
#Find the next minimal in the array and place it at the right position
#Advantage of select sort is in the fact, that we usually swap less (max n times) - this make it more efficient, but
#still quadratic (two loops inside of each other)
#Why do we swap less? we always find the next minimal, therefore in each swap we place one element at his final position,
#this means that (for n elements large aray) we cannot swap more than n times

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

array = [64, 12, 25, -4, 1, 55, -29, -12];
selectSort(array);
print(array);