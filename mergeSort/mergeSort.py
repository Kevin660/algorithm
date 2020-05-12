import sys
import math
try:
    file = open('unsorted1.txt', 'r')
    unsorted_list = file.read().split('\n')
except:
    print('file reading error')
    sys.exit()
    

#merge sort
# -- recursive
# 
# sys.setrecursionlimit(2000)
# def merge_sort(arr):
#     middle = (len(arr) + 1)//2
#     left = arr[0:middle]
#     right = arr[middle:]
#     if len(arr) <= 2: return merge(left, right)
#     return merge(merge_sort(left),merge_sort(right))

# def merge(left, right, result = []):
#     if len(left) == 0: return result + right
#     if len(right) == 0: return result + left
#     if int(left[0]) < int(right[0]):
#         return merge(left[1:], right ,result + left[0:1])
#     return merge(left, right[1:], result + right[0:1])

# for loop

def merge_sort(arr):
    level = int(math.log(len(arr), 2))
    # times
    for i in range(level):
        inteval = 2 ** i
        new_arr = []
        # merge
        for j in range(2 ** (level - i - 1)):
            # compare
            left = j * inteval * 2
            right = left + inteval
            end = right + inteval
            while(left < (j * inteval * 2 + inteval) and right < (j * inteval * 2 + inteval * 2)):
                if arr[left] > arr[right]: 
                    new_arr.append(arr[right])
                    right += 1
                else:
                    new_arr.append(arr[left])
                    left += 1
            while(right < (j * inteval * 2 + inteval * 2)):
                new_arr.append(arr[right])
                right += 1
            while(left < (j * inteval * 2 + inteval)):
                new_arr.append(arr[left])
                left += 1
        arr = new_arr
    return new_arr

print(merge_sort(unsorted_list))