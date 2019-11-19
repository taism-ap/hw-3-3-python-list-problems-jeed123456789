from random import randint
# find maximum integer in a list

# function that finds the maximum integer in a list
def find_maximum(arr):
    # initialize max that holds the maximum integer value in arr
    # connects max_num to 0 since the lowest possible number is 1
    max_num = 0
    # checks through every item in arr and compares it to max_num
    # if i is larger than max_num, replace max_num with i
    for i in arr:
        if(i > max_num):
            max_num = i
    # returns value of maximum integer value
    return max_num

# initialize an empty list, arr
arr = []

# append a random integer between 1 and 50 to arr 10 times
for i in range(10):
    arr.append(randint(1,50))

# assign maximum integer to max_num
max_num = find_maximum(arr)

print(arr) # print arr
print(max_num) # print max_num
