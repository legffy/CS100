# Import necessary modules
import hw5_util
import math

# Function to display grid with formatted string output and dimensions
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
# Function to retrieve valid neighbors in the grid
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
# Print neighbors for each start location in a grid
    if r-1 == -1: 
        neighbors.remove(d1)
    if c-1 == -1: 
        neighbors.remove(d2)
    if c+1 == nC:
        neighbors.remove(d3)
    if r+1 == nR:
        neighbors.remove(d4)
# Validate movement along a path within grid bounds and check elevation changes
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
# Identify the maximum height location in the grid
        cC = path[x][1]
        pR = path[x-1][0]
        pC = path[x-1][1]
        if cR < 0 or cC < 0 or cR > len(grid) -1 or cC > len(grid[0])-1 or abs(pR-cR) == 1 and abs(pC-cC) == 1:
            return ('Path: invalid step from {} to {}'.format(path[x-1],path[x]))
        if path[x-1][0] != path[x][0]:
            if grid[pR][cC] > grid[cR][cC]:
                d += abs(grid[pR][cC]-grid[cR][cC])
            elif grid[pR][cC] <= grid[cR][cC]:
                u += abs(grid[cR][cC]-grid[pR][cC])
        elif path[x-1][1] != path[x][1]:
# Retrieve highest valid neighbor for given location, based on step height
            if grid[cR][pC] > grid[cR][cC]:
                d += abs(grid[cR][pC]-grid[cR][cC])
            elif grid[cR][pC] <= grid[cR][cC]:
                u += abs(grid[cR][cC]-grid[cR][pC])
    down = 'Downward {}\n'.format(d)
    up = 'Upward {}'.format(u)
    return 'Valid path\n'+down+up
def findMaxHeight(i):
    grid = hw5_util.get_grid(i)
    maxHeight = 0 
    row, column = 0, 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] > maxHeight:
                row , column = r, c
# Retrieve lowest valid neighbor for gradual path, based on step height
                maxHeight = max(maxHeight,grid[r][c])
    return  (row,column), maxHeight
#neighbors
#the highest one can climb next
def findMaxNbr(n,h,rLen,cLen,i):
    grid = hw5_util.get_grid(i)
    nbrs = getNbrs(n[0],n[1],rLen,cLen)
    #max neighbor height
    maxNH = grid[n[0]][n[1]]
    diff = 0
    for x in range(len(nbrs)):
        cN = grid[nbrs[x][0]][nbrs[x][1]]
        if cN-maxNH <= h and cN-maxNH > 0 and cN-maxNH > diff:
            n = (nbrs[x][0],nbrs[x][1])
            diff = cN-maxNH
# Check if a given cell has the highest elevation among its neighbors
    return n
def findMinNbr(n,h,rLen,cLen,i):
    grid = hw5_util.get_grid(i)
    nbrs = getNbrs(n[0],n[1],rLen,cLen)
    #min neighbor height
    minNH = grid[n[0]][n[1]]
# Find steepest ascent path based on current height and step height
    diff = h+1
    for x in range(len(nbrs)):
        cN = grid[nbrs[x][0]][nbrs[x][1]]
        if cN-minNH <= h and cN-minNH > 0 and cN-minNH < diff:
            n = (nbrs[x][0],nbrs[x][1])
            diff = cN-minNH
    return n
def checkifMaxNeighbor(n,rLen,cLen,i):
    grid = hw5_util.get_grid(i)
    nbrs = getNbrs(n[0],n[1],rLen,cLen)
    for x in nbrs:
        if grid[x[0]][x[1]] > grid[n[0]][n[1]]:return False
    return True
#grid Index
#step height
def findSteepestPath(i,sH):
    grid = hw5_util.get_grid(i)
    cPath = ''
    sLoc = hw5_util.get_start_locations(i)
    paths = ['' for z in range(len(sLoc))]
    rLen = len(grid)
    cLen = len(grid[0])
    maxHeight = findMaxHeight(i)
    cHeight = (0,0)
    noneHigher = False
    cI = 0 
    pI = 0
    for l in sLoc:
        cPath = cPath + str(l)
        cHeight = l
        noneHigher = False         
        while grid[cHeight[0]][cHeight[1]] < maxHeight[1] and noneHigher == False:
            if cHeight == findMaxNbr(cHeight,sH,rLen,cLen,i):
                noneHigher = True
                if checkifMaxNeighbor(cHeight,rLen,cLen,i):
                    cPath = cPath + ' \nlocal maximum'
                else:
                    cPath = cPath + ' \nno maximum'
            else:
# Function to find the most gradual path for ascent
                cHeight = findMaxNbr(cHeight,sH,rLen,cLen,i)
                if cI < 4:
                    cPath = cPath +' ' +str(cHeight)
                    cI += 1
                    if grid[cHeight[0]][cHeight[1]] == maxHeight[1]:
                        cPath = cPath + ' \nglobal maximum'
                else:
                    cPath = cPath + ' \n' + str(cHeight)
                    cI = 0
                    if grid[cHeight[0]][cHeight[1]] == maxHeight[1]:
                        cPath = cPath + ' \nglobal maximum'
        paths[pI] = cPath
        cPath=''
        pI += 1
        cI = 0
    return paths

def findGradualPath(i,sH):
    grid = hw5_util.get_grid(i)
    cPath = ''
    sLoc = hw5_util.get_start_locations(i)
    paths = ['' for z in range(len(sLoc))]
    rLen = len(grid)
    cLen = len(grid[0])
    maxHeight = findMaxHeight(i)
    cHeight = (0,0)
    noneHigher = False
    cI = 0 
    pI = 0
    for l in sLoc:
        cPath = cPath +str(l)
        cHeight = l
        noneHigher = False         
        while grid[cHeight[0]][cHeight[1]] < maxHeight[1] and noneHigher == False:
            if cHeight == findMinNbr(cHeight,sH,rLen,cLen,i):
# Convert a string of tuples into actual tuple format
                noneHigher = True
                if checkifMaxNeighbor(cHeight,rLen,cLen,i):
                    cPath = cPath + ' \nlocal maximum'
                else:
                    cPath = cPath + ' \nno maximum'
            else:
                cHeight = findMinNbr(cHeight,sH,rLen,cLen,i)
# Create a grid representation based on path data
                if cI < 4:
                    cPath = cPath + ' ' +str(cHeight)
                    cI += 1
                    if grid[cHeight[0]][cHeight[1]] == maxHeight[1]:
                        cPath = cPath + ' \nglobal maximum'
                else:
                    cPath = cPath + ' \n' + str(cHeight)
                    cI = 0
                    if grid[cHeight[0]][cHeight[1]] == maxHeight[1]:
                        cPath = cPath + ' \nglobal maximum'
        paths[pI] = cPath
        cPath=''
        pI += 1
        cI = 0
    return paths
def stringToTuple(s):
    s = s.replace('\n',' ')
# Print the grid with marked path locations
    s = s.replace(', ',',')
    s = s.split()
    tupleList = []
    for t in s:
        if t.startswith('(') and t.endswith(')'):
            e = t.strip('()').split(',')
            tupleList.append((int(e[0].strip()),int(e[1].strip())))
    return tupleList
def pathGrid(s,g,i,sH):
    grid = hw5_util.get_grid(i)
# Main execution starts here, including grid selection, path finding, and optional path grid display
    rLen = len(grid)
    cLen = len(grid[0])
    pGrid = [['.'for c in range(cLen)] for r in range(rLen)]
    s =''
    sloc = hw5_util.get_start_locations(i)
    for paths in range(len(steepestPath)):
        s = s + ' ' +findGradualPath(i,sH)[paths]
        s = s + ' ' + findSteepestPath(i,sH)[paths]
    for row in range(rLen):
        for col in range(cLen):
            for x in stringToTuple(s):
                if (row, col) == x:
                    if pGrid[row][col] == '.':
                        pGrid[row][col] = 1
                    else:
                        pGrid[row][col]+=1
           
    return pGrid
def printGrid(g,i):
    grid = hw5_util.get_grid(i)
    rLen = len(grid)
    cLen = len(grid[0])
    print('Path grid')
    for row in range(rLen):
        for col in range(cLen):
            print('  {}'.format(g[row][col]), end ='')
            if col == cLen-1:
                print()


if __name__ == "__main__":
    gridIndex = 0
    while gridIndex > 3 or gridIndex < 1:
        gridIndex = input('Enter a grid index less than or equal to 3 (0 to end): ')
        print(gridIndex)
        gridIndex = int(gridIndex)
    sH = input('Enter the maximum step height: ')
    sH = int(sH)
    print(sH)
    pathgTorF =input('Should the path grid be printed (Y or N): ')
    print(pathgTorF)
    pathgTorF = pathgTorF.upper()
    r = len(hw5_util.get_grid(gridIndex))
    c = len(hw5_util.get_grid(gridIndex)[0])
    print('Grid has {} rows and {} columns'.format(r,c))
    maxHeight = findMaxHeight(gridIndex)
    print('global max: {} {}'.format(maxHeight[0],maxHeight[1]))
    steepestPath = findSteepestPath(gridIndex,sH)
    gradualPath = findGradualPath(gridIndex,sH)
    eqOrDot = 0
    for paths in range(len(steepestPath)):
        print('===')
        print('steepest path')
        print(steepestPath[paths])
        print('...')
        print('most gradual path')
        print(gradualPath[paths])
    print('===')
    if pathgTorF == 'Y':
        printGrid(pathGrid(steepestPath,gradualPath,gridIndex,sH),gridIndex)