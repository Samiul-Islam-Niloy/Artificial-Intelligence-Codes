neighbour = [('i', 'a', 35), ('i', 'b', 45), ('a', 'c', 20), ('a', 'd', 30),
             ('b', 'd', 25), ('b', 'e', 35), ('b', 'f', 27),
             ('c', 'd', 30), ('c', 'g', 47), ('d', 'g', 30), ('e', 'g', 25)]

visited = [0] * len(neighbour)


def pathLength(X, Y, L=[]):
    if X == Y:
        total_weight = sum(L)
        print("Total Length: ", total_weight)
        return

    i = 0
    child = ''
    while i <= len(neighbour) - 1:
        if visited[i] == 0 and neighbour[i][0] == X:
            visited[i] = 1
            child = neighbour[i][1]
            L.append(neighbour[i][2])
            pathLength(child, Y)

        i = i + 1

    if len(L) >= 1:
        L.pop()


# Main
start = str(input('Start Node: '))
goal = str(input('Destination Node: '))

pathLength(start, goal)
