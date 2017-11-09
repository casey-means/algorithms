#binary search

def binary_search(arr, val):
        first  = 0
        last = len(arr) - 1
        found = -1
        ctr = 0
        while first < last and found < 0:
               mid = (first + last) /2
               if arr[mid] == val:
                       found = mid
               elif arr[mid] > val:
                       print(arr[mid])
                       last = mid
               elif arr[mid] < val:
                        print(arr[mid])
                        first = mid + 1
               
        return found

test = [1,4,6,7,8,10]
rel = binary_search(test,7)


