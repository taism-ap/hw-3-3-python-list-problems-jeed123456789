from random import randint
# find minimum integer in a randomized list size 10

# function that finds the minimum integer in a list
def find_minimum(arr, max_number):
    # initialize min as 51 that will store minimum integer value
    min_num = max_number + 1

    # check through every integer value in arr and compare it to min_num
    # if i is smaller than min_num, replace min_num with i
    for i in arr:
        if(i < min_num):
            min_num = i
    return min_num
# initialize an empty list, arr
arr = []
max_number = 50
# add random integer between 1 and 50 to arr 10 times
for i in range(10):
    arr.append(randint(1, max_number))

# call function and assign minimum integer value to min_num
min_num = find_minimum(arr, max_number)

print(arr) # print arr
print(min_num) # print min_num
