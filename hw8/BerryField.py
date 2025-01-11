"""
Code was built with the intention of simulating what it is like having bears and tourists interact with each other in a berryf field
Randy Taylor
"""
class BerryField(object):
    #self, berryField, tourist locations, bear locations, reserve tourist locations, reserve bear locations, bear object and tourist object
    def __init__(self,bField,tlocs,blocs,rTlocs,rBlocs,bear,tourist):
        self.bF = bField
        self.tL = tlocs
        self.bL = blocs
        self.rTL = rTlocs
        self.rBL = rBlocs
        self.b = bear
        self.t = tourist
        #the dimensions of tje field
        self.rowL = len(self.bF)
        self.colL = len(self.bF[0])
        #total berry count
        self.bC = 0 
    #generates a string representation of the berryfield
    def __str__(self):
        field = ''
        bcount = 0
        #checks each instance of the berryField which is a 2d array and adds there number to and if there is a bear or tourist in that locations
        #it shows that instead
        for i in range(len(self.bF)):
            for j in range(len(self.bF[0])):
                bcount+=self.bF[i][j]
                if any(i==t[0] and j ==t[1] for t in self.tL) and any(i == l[0] and j ==l[1] for l in self.bL) :
                    field = field + '{:>4}'.format('X')
                elif any(i==t[0] and j ==t[1] for t in self.tL):
                    field =  field + '{:>4}'.format('T')
                elif any(i == l[0] and j ==l[1] for l in self.bL):
                    field = field + '{:>4}'.format('B')
                else:
                    field = field + '{:>4}'.format(self.bF[i][j])       
            field = field + '\n'
        field = field[:-1]
        self.bC = bcount
        #returns number of berries and the field count of people
        return'Field has {} berries.\n'.format(bcount)+ field
    #this was used to see the amount of berries in spots where there was tourists and bears
    def NoExtras(self):
        field = ''
        bcount = 0
        for i in range(len(self.bF)):
            for j in range(len(self.bF[0])):
                    bcount+=self.bF[i][j]
                    field = field + '{:>4}'.format(self.bF[i][j])
                   
            field = field + '\n'
            self.bC = bcount
        return'Field has {} berries.\n'.format(bcount)+ field
    #checks if the current square is valid or not
    def checkIfValid(self,y,x):
        return x>=0 and x < self.rowL and y >= 0 and y < self.colL
    #checks if the current square has 10 berries at the spot
    def checkIf10(self,x,y):
        if self.checkIfValid(x-1,y-1) and self.bF[x-1][y-1] == 10:
                return True
        if self.checkIfValid(x,y-1) and self.bF[x][y-1] == 10:
                return True
        if self.checkIfValid(x+1,y-1) and self.bF[x+1][y-1] == 10:
                return True
        if self.checkIfValid(x-1,y) and self.bF[x-1][y] == 10:
                return True
        if self.checkIfValid(x-1,y+1) and self.bF[x-1][y+1] == 10:
                return True
        if self.checkIfValid(x,y+1) and self.bF[x][y+1] == 10:
                return True
        if self.checkIfValid(x+1,y+1) and self.bF[x+1][y+1] == 10:
                return True
        if self.checkIfValid(x+1,y) and self.bF[x+1][y] == 10:
                return True
        return False
    #grows berries on the field based on certain requirments.
    #if a square has more than 0 berries and less than 10 then it grows 1 berry
    #if a square has 0 berries and a square next to it has 10 berries it grows 1 berry 
    def growField(self):
        zeros = []
        #does a first check and sees if any berries are between 0 and 10
        #adds any squares with no berries to a list
        for i in range(len(self.bF)):
            for j in range(len(self.bF[0])):
                if isinstance(self.bF[i][j], str):
                     pass
                elif self.bF[i][j]>= 1 and self.bF[i][j]<10:
                    self.bF[i][j]+=1
                elif self.bF[i][j] == 0:
                    zeros.append([i,j])
        #iterates through the list of 0 berries and checks if any of the sqaures around the berries has 10 berries
        for z in zeros:
             if self.checkIf10(z[0],z[1]):
                self.bF[z[0]][z[1]]+=1
                self.bC+=self.bF[z[0]][z[1]]
    #given a bear object it checks the current direction of said bears
    def bearDir(self,b):
        if  b[2]=='N':

            b[0]-=1

        if  b[2]=='E':

            b[1]+=1

        if  b[2]=='S':

            b[0]+=1

        if  b[2]=='W':

            b[1]-=1

        if  b[2]=='NE':

            b[1]+=1
            b[0]-=1
        
        if  b[2]=='NW':

            b[1]-=1
            b[0]-=1

        if  b[2]=='SE':

            b[1]+=1
            b[0]+=1

        if  b[2]=='SW':

            b[1]-=1
            b[0]+=1
    #determines if the movement of a bear has caused it to leave the field
    def bearOut(self):
        out = ''
        bL = self.bL[:]
    #iterates through a copy of the list bears and checks if they are in the field
    #the reason a copy is used is so that if a bear needs to be removed there is no index error
        for b in bL:
            if not self.checkIfValid(b[0],b[1]):
                out = out + 'Bear at ({},{}) moving {} - Left the Field\n'.format(b[0],b[1],b[2])
                self.bL.remove(b)
        #removes the extra \n at the end
        out = out[:-1]
        return out   
    #moves each bear on the field 
    #each bear moves in a certain direction till it has eaten 30 berries
    #doesn't move if it is asleep
    def bearMoves(self):
         for b in self.bL:
            count = 0
            while count < 30 and self.checkIfValid(b[0],b[1]):
                #stops running if bear is asleep
                if  b[3][str(b[2])] > 0:
                     break
                #stops running if bear is at the same spot as a tourist
                if b[:2] in [t[:2] for t in self.tL]:
                     break
                #calculates how many berries to remove from each spot
                adder = self.bF[b[0]][b[1]]
                self.bF[b[0]][b[1]]-=adder
                count+=adder
                #if amount of berries exceed 30 adds berries back to current spot
                if count >= 30:
                     self.bF[b[0]][b[1]]=count-30
                     break
                #if the code hasn't stopped up until this point the bear moves
                self.bearDir(b)
    #determines if a bear is range of the current tourists
    #uses magnitude of the distance between the two to figure it out
    #if bear is within 4 then tourist adds 1 to the count of bears around it 
    def tourDirCount(self,t):
        count=0
        for b in self.bL:
                  d = ((b[0]-t[0])**2+(b[1]-t[1])**2)**.5
                  if d<=4:
                       count+=1
        #   for b in self.bL:
     #           if abs(t[0]-b[0])+abs(t[1]-b[1])<=4:
     #             count +=1
        return count 
    #tourist determines if they leave or stay in field
    # if a tourist hasn't seen a bear for 3 turns they leave
    # if a tourist and a bear are on the same square they leave 
    # if a tourist sees 3 bears at the same time it leaves
    def bearCheck(self):
        out = ''
        tL = self.tL[:]
        #goes through copy of the tourist list so that there are no errors from removing anything
        for t in tL:
            for b in self.bL:
                #checks if a bear and tourist are in the same spot
                #puts bear to sleep for 3 turns
                if t[:2] == b[:2]:
                    b[3][str(b[2])] = 3
                    if t not in self.tL:
                         pass
                    else:
                        self.tL.remove(t)
                        out = out + 'Tourist at ({},{}), {} turns without seeing a bear. - Left the Field\n'.format(t[0],t[1],t[2])
            if t not in self.tL:
                 pass
            else:
                c = 0
                c+= self.tourDirCount(t)
                if c > 0:
                    t[2]=0
                else:
                     t[2]+=1
                #checks if there are more than three bears at once
                if c > 2:
                    self.tL.remove(t)
                    out = out+ 'Tourist at ({},{}), {} turns without seeing a bear. - Left the Field\n'.format(t[0],t[1],t[2])
                #checks if the tourist has gone 3 turns without seeing a bear
                if t[2] > 2:
                    self.tL.remove(t) 
                    out =out + 'Tourist at ({},{}), {} turns without seeing a bear. - Left the Field\n'.format(t[0],t[1],t[2])
        out = out[:-1]
        return out
    #puts reserve bears in if there are is enough reserve bears and more than 500 berries 
    def importBears(self):
        if len(self.rBL) >0 and self.bC > 500:
            self.bL.append(self.rBL[0])
            print('Bear at ({},{}) moving {} - Entered the Field'.format(self.rBL[0][0],self.rBL[0][1],self.rBL[0][2]))
            self.rBL.pop(0)
    #puts reserve bears in if there are enough reserve tourists and bears still in the field
    def importTourists(self):
        if len(self.rTL) > 0 and len(self.bL) >0:
             self.tL.append(self.rTL[0])
             print('Tourist at ({},{}), {} turns without seeing a bear. - Entered the Field'.format(self.rTL[0][0],self.rTL[0][1],self.rTL[0][2]))
             self.rTL.pop(0)  
    #ends simulations if there are no bears and reserve bears or  if there are no berries and no bears      
    def checkToEnd(self):
         check1 = len(self.bL) == 0 and len(self.rBL) == 0
         check2 = len(self.bL) == 0 and self.bC == 0 
         return check1 or check2