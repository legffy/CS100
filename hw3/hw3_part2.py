#function that dictates the pokemons location of a pokemon
def move_pokemon(column, row,direction, steps):
    if direction == 'N':
        column-=steps
    elif direction == 'S':
        column+=steps
    elif direction == 'W':
        row-=steps
    elif direction == 'E': 
        row+=steps
    row=min(row,150)
    row=max(0,row)
    column=min(column,150)
    column=max(0,column)
    return (column,row)
#reverses current direction of the pokemon
def oDirection(s):
    if s=='N': return 'S'
    if s=='S': return 'N'
    if s=='E': return 'W'
    if s=='W': return 'E'
#simulates fighting a pokemon
def pokeFight(c, r, n, di,rec):
    pokeT = input('What type of pokemon do you meet (W)ater, (G)round? => ')
    print(pokeT)
    pokeT=pokeT.upper()
#if pokemomn is ground type we run away 10 steps in the opposite direction
    if pokeT == 'G':
        di=oDirection(di)
        c, r=move_pokemon(c, r,di,10)
        rec.append('Lose')
        print('{0} runs away to ({1}, {2})'.format(name,c, r))
        return (c,r)
#if the pokemon is a water type we go foward in the same direction 1 step
    if pokeT == 'W':
        c, r=move_pokemon(c, r,di,1)
        rec.append('Win')
        print('{0} wins and moves to ({1}, {2})'.format(name,c, r))
        return (c,r)
#if user doesn't pick water or ground the nothing happens
    rec.append('No Pokemon')
    return (c,r)
if __name__ == "__main__":
    count=1
    record=[]
    y, x=75, 75
    d=''
    #Game begins
    #asks user how many turns they would like to play
    turns = int(input('How many turns? => '))
    print(turns)
    #asks user what the name of their pikachu is
    name = str(input('What is the name of your pikachu? => '))
    print(name)
    #asks user how often they want to run into another in pokemon
    spawnRate = max(int(input('How often do we see a Pokemon (turns)? => ')),0)
    print(spawnRate)
    print()
    #runs simulation
    print('Starting simulation, turn 0 {0} at ({1}, {2})'.format(name,y, x))
    while (turns+1) != count:
        d=input('What direction does {0} walk? => '.format(name))
        print(d)
        d=d.upper()
        y, x = move_pokemon(y, x, d, 5)
        if count % spawnRate == 0 and count>0:
            print('Turn {0}, {1} at ({2}, {3})'.format(count,name,y, x))
            y, x = pokeFight(y, x,name,d,record)
        count+=1
    
    print('{0} ends up at ({1}, {2}), Record: {3}'.format(name,y,x,record))