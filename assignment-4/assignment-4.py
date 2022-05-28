#sample data

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

'''
Sample data for Tic Tac Toe below:
'''

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

'''
Sample data for ETA below:
(from_stop, to_stop)
'''

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

import numpy as np

# Assignment 4
# This assignment covers your proficiency with Python's data structures.
# It engages your ability to manipulate and evaluate data stored in lists and dictionaries.
# '''
# 
#     '''
#     Item 1.
#     Relationship Status. 20 points.
#     Let us pretend that you are building a new app.
#     Your app supports social media functionality, which means that users can have
#     relationships with other users.
#     There are two guidelines for describing relationships on this social media app:
#     1. Any user can follow any other user.
#     2. If two users follow each other, they are considered friends.
#     This function describes the relationship that two users have with each other.
#     Please see "assignment-4-sample-data.py" for sample data. The social graph
#     will adhere to the same pattern.
#     Parameters
#     ----------
#     from_member: str
#         the subject member
#     to_member: str
#         the object member
#     social_graph: dict
#         the relationship data    
#     Returns
#     -------
#     str
#         "follower" if fromMember follows toMember,
#         "followed by" if fromMember is followed by toMember,
#         "friends" if fromMember and toMember follow each other,
#         "no relationship" if neither fromMember nor toMember follow each other.

    # Write your code below this line
def relationship_status(from_member, to_member, social_graph):

    from_member_following = social_graph[from_member]['following']
    to_member_following = social_graph[to_member]['following']
    
    if from_member in to_member_following and to_member in from_member_following:
        return "friends"
    elif to_member in from_member_following:
        return "follower"
    elif from_member in to_member_following:
        return "followed by"
    else:
        return "no relationship"
    
print(relationship_status("@bongolpoc", "@chums", social_graph))
print(relationship_status("@chums", "@bongolpoc", social_graph))
print(relationship_status("@jobenilagan", "@bongolpoc", social_graph))
print(relationship_status("@jobenilagan", "@joeilagan", social_graph))

#     Item 2.
#     Tic Tac Toe. 20 points.
#     Tic Tac Toe is a common paper-and-pencil game. 
#     Players must attempt to successfully draw a straight line of their symbol across a grid.
#     The player that does this first is considered the winner.
#     This function evaluates a tic tac toe board and returns the winner.
#     Please see "assignment-4-sample-data.py" for sample data. The board will adhere
#     to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
#     have more than one winner. The board will only ever have 2 unique symbols at the same time.
#     Parameters
#     ----------
#     board: list
#         the representation of the tic-tac-toe board as a square list of lists
#     Returns
#     -------
#     str
#         the symbol of the winner or "NO WINNER" if there is no winner
# 
    # Write your code below this line
def tic_tac_toe(board):

    transposed_board = [[row[_] for row in board] for _ in range(len(board[0]))]
    row_result = "".join(["".join(_) for _ in [list(set(row)) for row in board] if len(_) == 1])
    column_result = "".join(["".join(_) for _ in [list(set(row)) for row in transposed_board] if len(_) == 1])
    diagonal_result = "".join(["".join(_) for _ in [list(set(np.diagonal(board).copy()))] if len(_) == 1])
    other_diagonal_result = "".join(["".join(_) for _ in [list(set(np.fliplr(board5).diagonal().copy()))] if len(_) == 1])
    
    return row_result if row_result else column_result if column_result else diagonal_result if diagonal_result else other_diagonal_result if other_diagonal_result else "NO WINNER"
print(tic_tac_toe(board1))
print(tic_tac_toe(board2))
print(tic_tac_toe(board3))
print(tic_tac_toe(board4))
print(tic_tac_toe(board5))
print(tic_tac_toe(board6))

#     Item 3.
#     ETA. 25 points.
#     A shuttle van service is tasked to travel along a predefined circlar route.
#     This route is divided into several legs between stops.
#     The route is one-way only, and it is fully connected to itself.
#     This function returns how long it will take the shuttle to arrive at a stop
#     after leaving another stop.
#     Please see "assignment-4-sample-data.py" for sample data. The route map will
#     adhere to the same pattern. The route map may contain more legs and more stops,
#     but it will always be one-way and fully enclosed.
#     Parameters
#     ----------
#     first_stop: str
#         the stop that the shuttle will leave
#     second_stop: str
#         the stop that the shuttle will arrive at
#     route_map: dict
#         the data describing the routes
#     Returns
#     -------
#     int
#         the time it will take the shuttle to travel from first_stop to second_stop
# 
    # Write your code below this line

def eta(first_stop, second_stop, route_map):
    time_traveled = 0
    leg = [_ for _ in route_map.keys() if _[0] == first_stop][0]
    while leg[1] != second_stop:
        time_traveled += route_map[leg]['travel_time_mins']
        leg = [_ for _ in route_map.keys() if _[0] == leg[1]][0]
    time_traveled += route_map[leg]['travel_time_mins']
    
    return time_traveled

print(eta('upd', 'upd', legs))
print(eta('upd', 'admu', legs))
print(eta('admu', 'dlsu', legs))
print(eta('admu', 'upd', legs))
print(eta('upd', 'dlsu', legs))