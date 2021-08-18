# %% Function to return path value

def pathValue(startPoint, endPoint, cost=0):
    if (startPoint, endPoint) in pairList:
        print(str(cost + valueDict[(startPoint, endPoint)]) + ' ')

    for (i, j) in pairList:
        if i == startPoint:
            pathValue(j, endPoint, cost + valueDict[(i, j)])


# %% Input Handling and Calling recursive Function

valueDict = {('i', 'a'): 35, ('i', 'b'): 45, ('a', 'c'): 20, ('a', 'd'): 30,
             ('b', 'd'): 25, ('b', 'e'): 35, ('b', 'f'): 27, ('c', 'd'): 30,
             ('c', 'g'): 47, ('d', 'g'): 30, ('e', 'g'): 25}

pairList = [('i', 'a'), ('i', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'd'),
            ('b', 'e'), ('b', 'f'), ('c', 'd'), ('c', 'g'), ('d', 'g'),
            ('e', 'g')]

start = str(input('Enter Starting point: '))
end = str(input('Enter Ending point: '))

print('The length of path is: ')
pathValue(start, end)