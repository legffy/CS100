# Import necessary modules
import hw5_util
import math

# Define a function to display the grid with row and column information
#index
#show
def returnGrid(i,s):
    grid = hw5_util.get_grid(i)
    gridString = '  '
    r = len(grid)
    c = len(grid[0])
    for x in grid:
        for z in range(len(x)):
            if x[z] < 10:
                if len(x)-1 == z:
                    gridString = gridString+ ' ' + str(x[z])
                else:
                    gridString = gridString+ ' ' + str(x[z])+'  '
            else:
                if len(x)-1 == z:
                    gridString = gridString+ str(x[z])
                else:
                    gridString = gridString+ str(x[z])+'  '
        if x == grid[len(grid)-1]:
            gridString = gridString
        else:  
# Define a function to retrieve valid neighboring cells based on position and grid dimensions
            gridString = gridString + '\n  '
    if s == 'Y':
        print(gridString.rstrip())
    print('Grid has {} rows and {} columns'.format(r,c))
    return (r,c)

#row, column, number of Rows, number of Columns
def getNbrs(r, c, nR, nC):
    neighbors=[]
    neighbors.append((r-1,c))
    neighbors.append((r,c-1))
    neighbors.append((r,c+1))
    neighbors.append((r+1,c))
    d1 = (r-1,c)
    d2 = (r,c-1)
    d3 = (r,c+1)
    d4 = (r+1,c)
# Function to print neighbors for each start location in a grid
    if r-1 == -1: 
        neighbors.remove(d1)
    if c-1 == -1: 
        neighbors.remove(d2)
    if c+1 == nC:
        neighbors.remove(d3)
    if r+1 == nR:
        neighbors.remove(d4)
# Function to calculate the path with upward and downward movement validation
    return neighbors
#index
def giveNbrs(i):
    grid = hw5_util.get_grid(i)
    sLoc = hw5_util.get_start_locations(i)
    r = len(grid)
    c = len(grid[0])
    for x in sLoc:
        nbrs = getNbrs(x[0],x[1],r,c)
        nbrsF = ' '.join(str(nbr) for nbr in nbrs[:len(nbrs)])
        print('Neighbors of {0}: {1}'.format(x,nbrsF))
def findPath(i):
    path = hw5_util.get_path(i)
    grid = hw5_util.get_grid(i)
    d = 0
    u = 0
    for x in range(1,len(path)):
        cR = path[x][0]
# Main program execution starts here
        cC = path[x][1]
# Prompt user for grid index input and validate it
        pR = path[x-1][0]
        pC = path[x-1][1]
        if cR < 0 or cC < 0 or cR > len(grid) -1 or cC > len(grid[0])-1 or abs(pR-cR) == 1 and abs(pC-cC) == 1:
            return ('Path: invalid step from {} to {}'.format(path[x-1],path[x]))
        if path[x-1][0] != path[x][0]:
            if grid[pR][cC] > grid[cR][cC]:
# Prompt user to decide if the grid should be printed, then display grid and neighbors
                d += abs(grid[pR][cC]-grid[cR][cC])
            elif grid[pR][cC] <= grid[cR][cC]:
                u += abs(grid[cR][cC]-grid[pR][cC])
        elif path[x-1][1] != path[x][1]:
# Prints path calculation results for the specified grid index
            if grid[cR][pC] > grid[cR][cC]:
                d += abs(grid[cR][pC]-grid[cR][cC])
            elif grid[cR][pC] <= grid[cR][cC]:
                u += abs(grid[cR][cC]-grid[cR][pC])
    down = 'Downward {}\n'.format(d)
    up = 'Upward {}'.format(u)
    return 'Valid path\n'+down+up

if __name__ == "__main__":
    gridIndex = 0
    while gridIndex > 3 or gridIndex < 1:
        gridIndex = input('Enter a grid index less than or equal to 3 (0 to end): ')
        print(gridIndex)
        gridIndex = int(gridIndex)
    pYON = input('Should the grid be printed (Y or N): ')
    print(pYON)
    pYON = pYON.upper()
    if pYON == 'Y':
        print('Grid {}'.format(gridIndex))
    returnGrid(gridIndex,pYON)
    giveNbrs(gridIndex)
    print(findPath(gridIndex))
