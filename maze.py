'''maze = [
    ['S', 0, 1, 0],
    [1,   0, 1, 0],
    [1,   0, 0, 0],
    [1,   1, 1, 'E']
]'''
maze = [
    ['S', 0, 1, 0, 0, 0],
    [1,   0, 1, 0, 1, 0],
    [0,   0, 0, 0, 1, 0],
    [0,   1, 1, 0, 0, 0],
    [0,   0, 0, 1, 1, 0],
    [1,   1, 0, 0, 0, 'E']
]
#print(maze)
#print(len(maze))
#print(len(maze[0]))
def solve_maze(maze,row=0,col=0,visited=None):
    rows,cols=len(maze),len(maze[0])
    if visited is None:
        visited=set()
    if row<0 or row>=rows or col<0 or col>=cols or maze[row][col]==1 or (row,col) in visited:
        return None
    visited.add((row,col))
    if maze[row][col]=='E':
        return [(row,col)]
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    for dr,dc in directions:
        next_row,next_col=row+dr,col+dc
        path=solve_maze(maze,next_row,next_col,visited)
        if path is not None:
            return [(row,col)]+path
    return None
solution = solve_maze(maze)
print("Maze Solution Path:", solution)
