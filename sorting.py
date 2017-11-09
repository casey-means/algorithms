
#insertion sort
def insertionSort(Arr):
    for j in range(2,len(Arr)):
        key = Arr[j]
        i = j-1
        while(i>0 and Arr[i]>key):
            Arr[i+1] = Arr[i]
            i = i-1
        Arr[i+1]=key


def main():
    myList = [1,7,3,5,8,3,5,9,6,3,1,3,5,7,]
    insertionSort(myList)
    print(myList)

main()
