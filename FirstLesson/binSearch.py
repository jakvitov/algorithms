#Recursive search function to perform the actual search, if not present return -1
import math


def search(sequence, searchVal,start, end):
    if start > end:
        return -1;
    mid = math.floor(((start + end) / 2));
    #If the number is present in the middle of the array we return its value
    if (sequence[mid] == searchVal):
        return mid;
    #If the number is in the sequence is in the right half of the array we call this function
    # only on the right half of it
    elif (sequence[mid] > searchVal):
        return search(sequence, searchVal, start, mid);
    # If the number is in the sequence is in the left half of the array we call this function
    # only on the left half of it
    elif (sequence[mid] < searchVal):
        return search(sequence, searchVal, mid + 1, end);



#Using a binary serach algo find the given value in the given sequence and return its position
def binSearch (sequence):
    #We take and check the input if it's integer or not
    serachVal = input("Zadejte hledanou hodnotu: ");
    try:
        serachVal = int(serachVal);
    except:
        print("Nezadali jste celé číslo");
        return;

    position = search(sequence, serachVal, 0, len(sequence) - 1);
    if (position == -1):
        print("Číslo se v zadané posloupnosti nenachází.");
    else:
        print("Číslo se nachází na pozici: %d" % position);

sequence = [2, 5, 6, 8, 9, 11, 12, 15, 17, 19, 20, 21, 25, 29, 33, 38];
binSearch(sequence);
