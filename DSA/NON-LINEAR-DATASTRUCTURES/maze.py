'''Maze Problem'''
def maze_problem(maze):
    #printing Original maze
    print("Original Maze")
    for i in maze:
        for j in i:
            print(j,end=" ")
        print()
        
    # Creating resultant maze to store the path
    row = len(maze)
    col = len(maze[0])
    
    result = [[0 for j in range(col)] for i in range(row)]
    
    # Check the path is safe or not and traversing is in safer boundary or not
    def is_safe(x,y):
        if x >= 0 and x >= row: # in safe boundary or not
            return False
        elif y >= 0 and y >= col:   # in safe boundary or not
            return False
        elif maze[x][y] != 1:   # cell has the path or not
            return False
        return True
        
    def solution(x,y):
        if x == row - 1 and y == col - 1:
            if maze[x][y] != 1:
                return False
            result[x][y] = 1
            return True

        if is_safe(x,y):
            result[x][y] = 1
            if solution(x, y + 1):  # to move forward
                return True
            if solution(x + 1, y):  # to move downwards
                return True
            result[x][y] = 0
        return False
        
    if solution(0, 0):
        return result
    else:
        return "No Path Found"

maze = [
        [1, 1, 0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 1, 1, 1, 1]
]

res = maze_problem(maze)
print()
print("Path to reach the destination")
if isinstance(res,list):
    for i in res:
        for j in i:
            print(j,end=" ")
        print()
else:
    print(res)