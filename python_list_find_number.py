from random import randint
# count the number of times a supplied integer will appear in a list with 10 numbers

# function that can count the number of times a supplied integer will appear in a list with 10 numbers
def find_number(arr):
    count = 0 # initialize variable, count to track the number of times the integer appears

    #  add one to count every time the user input integer appears in the list
    for i in arr:
        if(i == num):
            count+=1
    return count
# receive number from user to check the number of times it appears in the list
num = int(input("Give me a number between 1 and 10 to search in the list: "))

# initialize an empty list named arr
arr = []

# appends a random integer to arr 10 times
for i in range(10):
    arr.append(randint(0,9))

print(arr) # print the array
count = find_number(arr) # call the function

print(count) # print count
