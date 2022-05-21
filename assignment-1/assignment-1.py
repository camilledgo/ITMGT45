# '''Assignment 1
# This assignment covers your basic profiency with
#     Python. It engages your ability to transform
#     data without affecting anything outside the program.
# This assignment places heavy emphasis on basic Python constructs.
# '''
# 
# def factorial(x):
#     '''Item 1. 
#     Factorial. 1 point.
#     
#     Returns the factorial of an integer.
#     An integer's factorial is the product of the integer and all
#         integers below it.
#     Parameters
#     ----------
#     x: int
#         the integer whose factorial to return
#     Returns
#     -------
#     integer
#         the factorial of the argument
#     '''
#     # Write your code below this line

def factorial(x):
    if x == 0:
        return(1)
    else:
        return int(x * factorial(x-1))

print(factorial(5))

# def classify_grade(number_grade):
#     '''Item 2.
#     Classify Grade. 2 points.
#     
#     Returns the letter grade equivalent of a number grade.
#     For this item, use these letter grade buckets:
#         A: 92-100
#         B+:86-91.9
#         B: 80-85.9
#         C+:74-79.9
#         C: 67-73.9
#         D: 60-66.9
#         F: 0-59.9
#     Parameters
#     ----------
#     number_grade: float
#         the number grade to convert into a letter grade.
#     Returns
#     -------
#     str
#         the letter grade equivalent of the number grade.
#     '''
#     # Write your code below this line

def classify_grade(number_grade):
    while number_grade > -1:
        if (number_grade >= 92) and (number_grade <= 100):
            return (str('A'))
        elif (number_grade >= 86) and (number_grade <= 91.9):
            return (str('B+'))
        elif (number_grade >= 80) and (number_grade <= 85.9):
            return (str('B'))
        elif (number_grade >= 74) and (number_grade <= 79.9):
            return (str('C+'))
        elif (number_grade >= 67) and (number_grade <= 73.9):
            return (str('C'))
        elif (number_grade >= 60) and (number_grade <=66.9):
            return (str('D'))
        elif (number_grade <= 59.9) and (number_grade > -1):
            return (str('F'))
print(classify_grade(77))
 
# def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
#     '''Item 3.
#     Average Weight. 3 points.
#     
#     You have purchased two bags of items. 
#     The first bag contains one type of item, and the second bag contains another type.
#     Return the weighted average weight of the items.
#         
#     Parameters
#     ----------
#     item_quantity_1: int
#         the quantity of items in the first bag.
#     item_weight_1: float
#         the weight of each individual item in the first bag.
#     item_quantity_2: int
#         the quantity of items in the second bag.
#     item_weight_2: float
#         the weight of each individual item in the second bag.
#     Returns
#     -------
#     float
#         the weighted average weight of one item.
#     '''
#     # Write your code below this line

def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    x = int(item_weight_1 + item_weight_2)
    y = float(item_quantity_1 + item_quantity_2)
    z = x / y
    return z

print (average_weight(3, 55.5, 4, 70.9))
    
# def string_sum(string):
#     '''Item 4.
#     String Sum. 3 points.
#     
#     Returns the sum of the digits provided in a string.
#     For this item:
#         1. Sum the digits contained in the string.
#         2. Ignore any non-digit characters contained in the string.
#     Parameters
#     ----------
#     string: str
#         a string that can contain any character.
#     Returns
#     -------
#     int
#         the sum of the digits contained in the string.
#     '''
#     # Write your code below this line

def string_sum(string):
    word = list(string)
    num = []
    for i in word:
        if (i.isdigit()):
            num.append(i)
    numnum = map(int, num)
    return sum(numnum)

print(string_sum("587249yyy"))
 
# def distance(x_1, y_1, x_2, y_2):
#     '''Item 5.
#     Distance. 3 points.
#     Returns the distance between two points.
#     To get the distance between two points:
#         1. Get the difference between the two x-coordinates
#         2. Get the difference between the two y-coordinates
#         3. Sum the previous two values
#         4. Return the square root of the sum
#     You may want to import the `math` library for this number.
#     Parameters
#     ----------
#     x_1: float
#         the first x-coordinate
#     y_1: float
#         the first y-coordinate
#     x_2: float
#         the second x-coordinate
#     y_2: float
#         the second y-coordinate
#     Returns
#     -------
#     float
#         the distance between the two coordinates
#     '''
#     # Write your code below this line

import math

def distance(x_1, y_1, x_2, y_2):
    dist1 = float(x_1 + x_2)
    dist2 = float(y_1 + y_2)
    dist_sum = dist1 + dist2
    square = math.sqrt(dist_sum)
    return float(square)

print(distance(2,3,2,3))
    
# def make_change(amount):
#     '''Item 6.
#     Make Change. 5 points.
#     
#     Return the combination of coins needed to make change for the given amount,
#         which is given in centavos.
#     For this item:
#         1. You can return 1 peso, 25 centavos, 10 centavos, 5 centavos, and 1 centavo coins.
#         2. Use the minimum number of coins possible.
#     Parameters
#     ----------
#     amount: int
#         the amount, in centavos, to make change for.
#     Returns
#     -------
#     str
#         the string representation of the change to be given.
#         Format it like this:
#             "1P:{amount}/25C:{amount}/10C:{amount}/5C:{amount}/1C:{amount}"
#     '''
#     # Write your code below this line

def make_change(amount):    
    amt = amount
    
    P1 = 0
    C25 = 0
    C10 = 0
    C5 = 0
    C1 = 0
    
    while amt >= 100:
       P1 = P1 + 1
       amt -= 100
    
    while amt >= 25:
        C25 = C25 + 1
        amt -= 25
        
    while amt >= 10:
        C10 = C10 + 1
        amt -= 10
     
    while amt >= 5:
        C5 = C5 + 1
        amt -= 5
    
    C1 = 0
    while amt >= 1:
        C1 = C1 + 1
        amt -= 1
        
    return "1P:{"+str(P1)+"}/25C:{"+str(C25)+"}/10C:{"+str(C10)+"}/5C:{"+str(C5)+"}/1C:{"+str(C1)+"}"

print(make_change(567))
    
    
    