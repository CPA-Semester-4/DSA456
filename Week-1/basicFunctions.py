# Write a function that is given and return the sum all numbers from 1 to n
def sum(n):
    rc = n
    rc = rc + n
    return rc

# this function returns the sum of the values inside array
def add(array):
    rc = 0
    # range function generates a list of values
    # in this case it reutrns 0 through length of array -1
    for i in range(len(array)):
        rc += array[i]
    return rc

def changeArray(array):
    print(array)
    temp = [6, 3, 2, 6]
    j = 0
    for i in temp:
        array[j] = i
        j += 1
    print(array)

# Calling a function
mylist = [3, 1, 6, 5, 2]
result = add(mylist)
print(result)
print(sum(5))
changeArray(mylist)
            