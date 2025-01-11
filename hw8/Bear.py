'''
Bear class in Berry field
Randy Taylor
'''
class Bear(object):
    #self, bears, and reserve bears
    def __init__(self,bears,reserves):
        self.bs = bears
        self.res = reserves
        #creates variable to count tunrs asleep
        for b in self.bs:
            b.append({str(b[2]): 0 for b in self.bs })
        for r in self.res:
            r.append({str(r[2]): 0 for r in self.res })
    #reports active bears and whether they are asleep or not
    def __str__(self):
        bears = 'Active Bears:\n'
        for b in self.bs:
            b[3][str(b[2])]-=1
            if b[3][str(b[2])] > 0:
                bears = bears + 'Bear at ({},{}) moving {} - Asleep for {} more turns\n'.format(b[0],b[1],b[2],b[3][str(b[2])])
            else:
                bears = bears + 'Bear at ({},{}) moving {}\n'.format(b[0],b[1],b[2])
        #removes extra \n
        bears = bears[:-1]
        return bears
    #checks if bear is on a valid square
    def checkIfValid(self,x,y,rowL,colL):
        return x>=0 and y < rowL and y >= 0 and x < colL
    #checks if a bear is on the given square
    def bearIsThere(self,x,y):
        count = 0
        bs = self.bs[:]
        for b in bs:
            if x == b[0] and y == b[1]:
                count+=1
        return count
    