from random import randint
# create a function called partition()
# This will take in some integer value and place all of the elements which are smaller on one side of the list, leaving the larger elements on the other

# function that takes in some integer value and place all of the elements which are smaller on one side of the list, leaving the larger elements on the other
def partition(arr, num):
    result = []  # create a result list that will have arr partitioned
    smaller = [] # create a list that has numbers smaller than chosen number
    larger = [] # create a list that holds numbers largers than chosen number
    count = len(arr) # create variable count to check how many num is in the list

    # goes through every element in arr
    for i in arr:
        # if i is larger than the chosen number, add it to smaller and decrease value of count by 1
        if(i < num):
            smaller.append(i)
            count = count - 1
        # if i is larger than the chosen number, add it to larger and decrease value of count by 1
        elif(i > num):
            larger.append(i)
            count = count - 1

    result = result + smaller # add smaller to result

    # add the chosen number (count times)
    for i in range(count):
        result.append(num)

    result = result + larger # add larger to result

    return result # return result list

arr = [] # initialize empty list, arr

# appends a random integer to arr 10 times
for i in range(10):
    arr.append(randint(0,40))
print(arr) # print arr

num = arr[randint(0,10)] # chooses a random number within the list
print(num) # print num, the number that is chosen

result = partition(arr, num) # call the partition function and assign the partitioned list to result
print(result) # print the partitioned list
