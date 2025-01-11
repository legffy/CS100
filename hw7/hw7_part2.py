import json
'''
code takes a dictionaries of movies and ratings and lets the user know about a genre of their choice based on a time period of their choice
Randy Taylor
'''
#takes movies and ratings as dictionaries
def filterRatings(m,r):
    #creates copys so that the originals aren't altered
    nM = m.copy()
    nR = r.copy()
    #the goal is to check if the amount of ratings in the ratings dictionary is greater than 2 ratings
    for x in r:
        if len(nR[x]) < 3:
            if x not in nM:
                del nR[x]
            else:
                del nR[x]
                del nM[x]
        elif x not in nM:
                del nR[x]
    #returns ratings and movies as a tuple
    return (nM,nR)
#creates a set of all genres once it reaches the max amount of genres it breaks
def findAllGenres(m):
    g = set()
    for x in m:
        for ge in m[x]['genre']:
            if ge not in g:
                g.add(ge)
            if len(g) == 23:
                break
    return g
#takes movies and ratings as dictionaries
#takes genre as a string
def filterGenres(m,r,g):
    #creates copys so that the orignials don't get altered
    nM = m.copy()
    nR = r.copy()
    #if the dictionary doesn't contain the genre gets rid of the instance from ratings and movies
    for x in m:
        if x not in nR:
            del nM[x]
        else:
            if g not in nM[x]['genre']:
                del nM[x]
                del nR[x]
    #returns ratings and movies as a tuple
    return (nM,nR)
#takes movies and ratings as dictionaries
#takes low and high as numbers for what the time period to filter movies
def filterDates(m,r,low,high):
    #creates copys to not alter the originals
    nM = m.copy()
    nR = r.copy()
    #deletes if the movie year from movies is not within low and high
    for x in m:
        date = nM[x]['movie_year']
        if x not in nR:
            del nM[x]
        elif date>high or date<low:
            del nM[x]
            del nR[x]
    return (nM,nR)
#given movies and ratings as dictionaries
#uses w1 and w2 as weights
#using a given formula the function calcutes the a rating for each movie in the given movies dictionary
def calculateScores(m,r,w1,w2):
    fD = dict()
    for x in m:
        if x not in r:
            pass
        else:
            imdbS = m[x]['rating']
            twitS = sum(r[x])/len(r[x])
            fD[x] = (w1 *imdbS + w2 *twitS)/(w1+w2)
    return fD
#finds the highest and lowest rated movie in a given dictionary
#takes a dictionary of movies and dictionary of scores
def getHighestAndLowest(m,s):
    l = []
    maxKey = None
    minKey = None
    #adds a tuple filled with the score based off the name in movies
    for x in s:
        l.append((s[x],m[x]['name']))
    #sorts the list based off this
    l = sorted(l, reverse = True)
    #for key and value in s checks if it is the highest or lowest value
    #based off this gives the key off the highest
    for k, v in s.items():
        if v == l[0][0]:
            maxKey = k
        if v == l[-1][0]:
            minKey = k
    #gets attributes based off the high and low of this 
    #then prints out these values in a nice format
    maxValue = s[maxKey]
    maxName = m[maxKey]['name']
    maxYear = m[maxKey]['movie_year']
    minValue = s[minKey]
    minName = m[minKey]['name']
    minYear = m[minKey]['movie_year']
    print('Best:')
    print('        Released in {}, {} has a rating of {:.2f}'.format(maxYear,maxName,maxValue))
    print()
    print('Worst:')
    print('        Released in {}, {} has a rating of {:.2f}'.format(minYear,minName,minValue))

if __name__ == "__main__":
    #reads the movies file
    movies = json.loads(open("movies.json").read())
    #reads the ratings file
    ratings = json.loads(open("ratings.json").read())
    #gets the minimum year
    minYear = max(int(input('Min year => ').strip()),.1)
    print(minYear)
    #gets the maximum year
    maxYear = int(input('Max year => ').strip())
    print(maxYear)
    #gets the weight the user wants to place on wIMDB
    wIMDB = input('Weight for IMDB => ').strip()
    print(wIMDB)
    wIMDB = float(wIMDB)
    #gets the weight the user wants to put on twitter
    wTwitter = input('Weight for Twitter => ').strip()
    print(wTwitter)
    wTwitter = float(wTwitter)
    print()
    check = ''
    while check != 'stop':
        #gets what genre user wants to see the highest and lowest rated movies for
        genre = input('What genre do you want to see? ').strip()
        print(genre)
        genre = genre.title()
        check = genre
        #filters based on this gnre
        nMovies, nRatings = filterRatings(movies,ratings)
        nMovies, nRatings = filterGenres(nMovies,nRatings,genre)
        nMovies, nRatings = filterDates(nMovies,nRatings,minYear,maxYear)
        #if the user wants to stop, program ends
        if check == 'Stop': 
            break
        #if the genre entered doesn't exist loops back
        elif genre not in findAllGenres(nMovies):
            print()
            print('No {} movie found in {} through {}'.format(check,minYear,maxYear))
            print()
        #if a valid genre is entered tells user about the highest and lowest rated movie in said genre
        else:
            print()
            getHighestAndLowest(nMovies,calculateScores(nMovies,nRatings,wIMDB,wTwitter))
            print()
        