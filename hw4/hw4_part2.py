import hw4_util
"""
code gets user input and answers questions about quarantine during certain weeks
"""
#returns a list with strings of a every state abbreveation
def getStates(i):
    states = []
    for x in range(0,52):
        states.append(hw4_util.part2_get_week(i)[x][0])
    return states
# option 1: returns the average number of positive cases over a given week or
# option 2: returns the average percent of positive test over a given week
# a is a list of the information based on a given week/index
# o is the state we want to get the information from
# c lets us know whether we want to return option 1 or 2
def avgCases(a,o,c):
    #average positive cases in a given week
    avgP = 0
    #average negative cases in a given week
    avgN = 0
    for x in range(2,9):
        avgP += a[o][x]
    for x in range(9,16):
        avgN += a[o][x]
    avgP = avgP/7
    avgN = avgN/7
    if c == 'pos': return avgP 
    elif c == 'total': return avgP/(avgP+avgN)*100

#checks whether or not there are more than 10 cases per week for every 100k people
#or if the percent of postive test in a state is greater than 10 percent
#s is a 2d list of the number of 
#i is the state we are looking over
def checkSpread(s,i):
    a100k = s[i][1]/100000
    avg = avgCases(s,i,'pos')
    avgPer100k = avg/a100k
    percent = avgCases(s,i,'total')
    if avgPer100k > 10 or percent > 10: return True
    return False
# main function that gives quaratine stats based off a index and request
# i = index
# r = request
def findDPQOrH(i,r):
# weeksData is the list for the index of the week
    weeksData = hw4_util.part2_get_week(i)
#Gives average daily positives per 100k population based on state
    if r == 'daily':
#ask for state input and makes it upper so there are no issues
        state = input('Enter the state: ')
        state = state.upper()
        print(state)
#if they enter something that isn't a state lets user know state not found
        if state not in getStates(i):
            print('State {0} not found'.format(state))
#Section that gives average daily positives per 100k for the state and index
        else:
            #state name
            sN = -1
            #Gets index of state inputted
            for x in range(0,52):
                if weeksData[x][0] == state: sN = x
            aDP = avgCases(weeksData,sN,'pos')/(weeksData[sN][1]/100000)
            print('Average daily positives per 100K population: {:.1f}'.format(aDP))
#Gives average percent of daily positives
    if r == 'pct':
#ask for state input and makes it upper so there are no issues
        state = input('Enter the state: ')
        print(state)
#if they enter something that isn't a state lets user know state not found
        if state not in getStates(i):
            print('State {0} not found'.format(state))
#section that gets average percent of daily positives
        else:
            #state name
            sN = -1
            #Gets index of state inputted
            for x in range(0,len(weeksData)):
                if weeksData[x][0] == state: sN = x
            aDPP =avgCases(weeksData,sN,'total')
            print('Average daily positive percent: {:.1f}'.format(aDPP))
#if request is quar finds all quarantined sates
    if r == 'quar':
        states = []
        for x in range(len(weeksData)):
            if checkSpread(weeksData,x): states.append(weeksData[x][0])
        print('Quarantine states:')
        hw4_util.print_abbreviations(states)
#if request is high finds the state with the highest amount of cases per 100k people
    if r == 'high':
        highI = 0
        high =avgCases(weeksData,0,'pos')/(weeksData[0][1]/100000)
        for x in range(len(weeksData)):
            if avgCases(weeksData,x,'pos')/(weeksData[x][1]/100000) > high:
                high = avgCases(weeksData,x,'pos')/(weeksData[x][1]/100000)
                highI = x
        print('State with highest infection rate is {0}'.format(weeksData[highI][0]))
        print('Rate is {:.1f} per 100,000 people'.format(high))   
if __name__ == "__main__":
    inde = 1
    requests =['daily', 'pct', 'quar', 'high']
#makes sure index is within the amount of states in the us
    while inde > 0 and inde < 52:
        print('...')
        inde = input('Please enter the index for a week: ')
        print(inde)
        inde = int(inde)
#ends if inde isn't in range
        if inde < 0 or inde > 51: break
#if there's no data for a given week reports that theres no data
        elif hw4_util.part2_get_week(inde) == []: 
            print('No data for that week') 
#ask for request
        else:
            request = input('Request (daily, pct, quar, high): ')
            print(request)
            request = request.lower()
#if request is in request gets info the quarantine issues in the united states based on a given week index and request
            if request in requests:
                findDPQOrH(inde,request)
#if request is not one of the four main request lets user know
            else:
                print('Unrecognized request')