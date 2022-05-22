# ''Assignment 2
# This assignment covers your intermediate profiency with
#     Python. It engages your ability to transform
#     data without affecting anything outside the program.
# This assignment places heavy emphasis on Python data structures.
# '''
# 
# def specific_filter(l):
#     '''Item 1.
#     Specific Filter. 2 points.
#     Returns the elements of a list that are greater than the integer 50.
#     This is called "filtering" each number based on whether it is greater than 50. 
#         Filtering is a very common pattern in high-level (i.e., human-readable)
#         programming.
#     For this number:
#         1. The parameter l will be a list of either floats or ints.
#     
#     Parameters
#     ----------
#     l: list
#         a list of numbers (floats or ints)
#     Returns
#     -------
#     list
#         a list of elements in l that are greater than the integer 50
#     '''
#     # Write your code below this line

def specific_filter(l):
    new = []
    for x in l:
        if x > 50:
            new.append(x)
    return new

print (specific_filter([1,89,66,3,4,99]))
                
# def general_filter(l, filter_function):
#     '''Item 2.
#     General Filter. 3 points.
#     Returns the elements of a list that return True when passed to a filtering function.
#     This is how general filters are done.
#     For this number:
#         1. The parameter l will be a list of any data type.
#         2. The filter_function is just a function that has been passed as an argument to 
#             the general_filter function. It accepts a single argument and returns either
#             True or False.
#     
#     Parameters
#     ----------
#     l: list
#         a list of any data type
#     filter_function: function
#         a function which accepts any data type and returns bool
#     Returns
#     -------
#     '''
#     # Write your code below this line

def general_filter(l, filter_function):
    x = map(filter_function, l)
    return list(x)

def filter_function(x):
    if type(x) is str:
        return True
    else:
        return False

print(general_filter([2, "home", 66.7, 7],filter_function))
    
# def specific_map(l):
#     '''Item 3.
#     Specific Map. 2 points.
#     Accepts a list of numbers. Returns another list which contains the squares of the
#         numbers.
#     This is called "mapping" each number to its square. Mapping is a very common pattern
#         in high-level (i.e., human-readable) programming.
#     For this number:
#         1. The parameter l will be a list of either floats or ints.
#     Example:
#     specific_map([1, 2, 3, 4, 5]) -> [1, 4, 9, 16, 25]
#     
#     Parameters
#     ----------
#     l: list
#         a list of numbers (floats or ints)
#     Returns
#     -------
#     list
#         a list of the squares of the elements in l
#     '''
#     # Write your code below this line

def result(x):
    return x * x

def specific_map(l):
    x = map(result, l)
    return list(x)

print(specific_map([1, 2, 3, 4, 5]))    
    
# 
# def general_map(l, map_function):
#     '''Item 4.
#     General Map. 3 points.
#     Accepts a list of any data type. Returns another list which uses a function to map
#         the first lists's elements to the second list.
#     This is how general maps are done.
#     
#     Parameters
#     ----------
#     l: list
#         a list of any data type
#     map_function: function
#         a function which accepts one argument and returns any data type
#     Returns
#     -------
#     list
#         a list which contains the mapped elements of l
#     '''
#     # Write your code below this line

def map_function(x):
    y = str(x)
    return y + y

def general_map(l, map_function):
    x = map(map_function, l)
    return list(x)

print(general_map(["happy", 2, 3.01, 4, "sad"],map_function))
