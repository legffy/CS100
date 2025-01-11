'''
Tourists Class in Berry Field
Randy Taylor
'''
class Tourist(object):
    #self tourists reserve tourists
    def __init__(self,tourists,reserves):
        self.tour = tourists
        self.res = reserves
        #adds a variablew to check how many turns a tourist has gone with out seeing a bear
        for t in self.tour:
            t.append(0)
        for r in self.res:
            r.append(0)
    #provides situatuon about a tourists current situation
    def __str__(self):
        tourists = 'Active Tourists:\n'
        for t in self.tour:
            tourists = tourists + 'Tourist at ({},{}), {} turns without seeing a bear.\n'.format(t[0],t[1],t[2])
        tourists = tourists[:-1]
        return tourists