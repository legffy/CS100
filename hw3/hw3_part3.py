import math
#calculates the amount of tourists based off a given amount of bears
def calcTourists(bears):
    if bears>15 or bears<4:
        return 0
    elif bears<11:
        return bears*10000
    else:
        return 100000+(bears-10)*20000
#finds berrys and beasrs after a year
def find_next(bears, berries, tourists):return int(berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1)),max(0,((berries*1.5) - (bears+1)*(berries/14) - (math.log(1+tourists,10)*0.05)))
#starts running bear simulation
#asks user for number of bears
if __name__ == "__main__":
    numBears =max(0,int(input('Number of bears => ')))
    print(numBears)
    #asks user for how big the berry araea is 
    berryArea =input('Size of berry area => ')
    print(berryArea)
    berryArea=max(0,float(berryArea))
    tourists=calcTourists(numBears)
    weBears=[numBears]
    weBerries=[berryArea]
    weTourists=[tourists]
    #Gives user stats over the years
    print('Year      Bears     Berry     Tourists  ')
    print('1{3}{0}{4}{1:.1f}{5}{2}{6}'.format(numBears,berryArea,tourists,(9*' '),(10-len(str(numBears)))*' ',(8-len(str(int(berryArea))))*' ',(10-len(str(tourists)))*' '))
    for x in range(2,11):
        numBears, berryArea=find_next(numBears,berryArea,tourists)
        tourists=calcTourists(numBears)
        weBears.append(numBears)
        weBerries.append(berryArea)
        weTourists.append(tourists)
        print('{3}{4}{0}{5}{1:.1f}{6}{2}{7}'.format(numBears,berryArea,tourists,x,(10-len(str(x)))*' ',(10-len(str(numBears)))*' ',(8-len(str(int(berryArea))))*' ',(10-len(str(tourists)))*' ')) 
    print()
    #gives user the max and min for bearss berrys and tourists
    print('Min:      {0}{3}{1:.1f}{4}{2}{5}'.format(min(weBears),min(weBerries),min(weTourists),(10-len(str(min(weBears))))*' ',(8-len(str(int(min(weBerries)))))*' ',(10-len(str(min(weTourists))))*' '))
    print('Max:      {0}{3}{1:.1f}{4}{2}{5}'.format(max(weBears),max(weBerries),max(weTourists),(10-len(str(max(weBears))))*' ',(8-len(str(int(max(weBerries)))))*' ',(10-len(str(max(weTourists))))*' '))