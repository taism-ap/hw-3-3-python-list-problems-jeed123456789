from random import randint
# function sort() which will sort the list from smallest to largest

# this specific sort is called the mergesort where the list is divided into twos until there is only one object and merging them back in order
# The following url is a link to a video that graphically shows the mergesort method
# https://www.youtube.com/watch?v=JSceec-wEyw
def sort(arr):

    # divide the list into two smaller lists if the length of the list is longer than one
    if len(arr) > 1:
        # find the middle index and assign that value to variable, mid_index
        mid_index = int(len(arr)/2)

        # create two lists, L and R, each one is arr divided from 0 to mid_index or mid_index to len(arr)-1
        L = arr[:mid_index]
        R = arr[mid_index:]

        # call the mergesort funciton again for each list, L and R.
        sort(L)
        sort(R)

        # create index_left, index_right, index_arr to keep tract of index of each list when comparing them and putting it into arr
        index_left = 0
        index_right = 0
        index_arr = 0

        # compare integers in L and R
        # The smaller integer is transfered into index_arr
        # If the two integers that are compared are same, add them both to the arr
        while index_left < len(L) and index_right < len(R):
            if L[index_left] > R[index_right]:
                arr[index_arr] = R[index_right]
                index_right+=1
            elif L[index_left] < R[index_right]:
                arr[index_arr] = L[index_left]
                index_left+=1
            else:
                arr[index_arr] = L[index_left]
                index_left+=1
                index_arr+=1
                arr[index_arr] = R[index_right]
                index_right+=1
            index_arr+=1

        # transfer the integers that were not addded to the array because it was the largest integer out of the integers in both lists
        # if the index of R and L is not same as the length of each list, that means that the last integer in that list is not transfered into the arr
        while index_left != len(L):
            arr[index_arr] = L[index_left]
            index_arr+=1
            index_left+=1
        while index_right !=  len(R):
            arr[index_arr] = R[index_right]
            index_arr+=1
            index_right+=1
        return arr # return arr

arr = [] # initialize empty list
num = 10 # assign size of the list arr to num

# create a randomized list
for i in range(num):
    arr.append(randint(0,40))

print("This is initial list:",arr) # print the initial list before sorting
arr = sort(arr) # call the sort method and sort the list
print("This is sorted list:", arr) # print the sorted list
