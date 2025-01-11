
#this funcition takes the name of a text file t and generates and returns a string based on that text file
def textToString(t):
    s = ''
    for line in open(t, encoding = 'utf-8'):
        s = s+line
    return s
#this function takes a string and first splits it into a list of words
#then it goes through it and replaces all non alpha characters with nothing 
#so if the sequence of characters aren't letters it takes them out of the list and returns a list of just  words
def splitTostr(s):
    l = s.split()
    for w in range(len(l)):
        for let in l[w]:
            if not(let.isalpha()):
                l[w] = l[w].replace(let,'')
        l[w] = l[w].lower()
    fL = [i for i in l if i != '' ]
    return fL
#takes a list and returns the average length of each instance and in this case each instance would be a word
def getAvgWordLen(l):
    total = 0
    for w in l:
        total += len(w)
    return total/len(l)
#checks the amount of distinct words in a list and finds the ratio of that to the average
def distinctToTotal(l):
    #tracking the amount of words in the list
    total = 0
    #distinct word list
    d =[]
    #word
    for w in l:
        total+=1
        #word isn't already in the distinct word list then we add it into the list
        if w not in d:
            d.append(w)
    #the amount of distinct words divided by the total amount of wordd
    return len(d)/total
#create a dictionary of sets which words at each length from 1 until that amount of words doesn't exist
def lenofWords(l):
    wordsLen = dict()
    for w in range(1,len(max(l, key = len))+1):
        wordsLen[w] = set()
    for w in l:
        wordsLen[len(w)].add(w)
    return wordsLen
#generates a string from a dictionary of sets of words a certain length
#if the set is a certain length then it will print all the words in that set the amount and length of the words
#if the amount of words is greater than 6 than it will print the first three and last three based off of alphabetic order
def wordsSorted(d):
    s =''
    last = list(d.keys())[-1]
    for num in sorted(d.keys()):
        if len(d[num]) < 7:
            words = ''
            for x in sorted(d[num]):
                words = words + ' ' + x
            if num == last:
                s = s +'{:4}:{:4}:{}'.format(num,len(d[num]),words)
            else:
                s = s +'{:4}:{:4}:{}\n'.format(num,len(d[num]),words)
        else:
            words = ''
            setofWord = sorted(d[num])
            for x in setofWord[:3]:
                words = words + ' ' + x
            words = words + ' ...' 
            for x in setofWord[-3:]:
                  words = words + ' ' + x
            if num == last:
                s = s + '{:4}:{:4}:{}'.format(num,len(d[num]),words)
            else:
                s = s + '{:4}:{:4}:{}\n'.format(num,len(d[num]),words)
    return s
#takes a list and max seperation
#based off this list it check all word pairs within mS
#if the word pair is unique it gets added to one list if not it gets added to the total 
#at the end a list of both list is returned
def distinctWordPairs(l,mS):
    pairs = []
    dPairs = []
    for w in range(len(l)-1):
        for sep in range(w+1,min(len(l),w+mS+1)):
            t = tuple(sorted((l[w],l[sep])))
            pairs.append(t)
            if t not in dPairs:
                dPairs.append(t)
    return [sorted(dPairs),pairs]
#takes a list of distinct word pairs and prints them out
#if the amount is less than ten the they just get printed out
#if the amount is greater than or equal to ten then it prints the first and last 5 based on alphabetic order
def pairsF5L5(l):
    s =''
    if len(l) < 10:
        for wP in l:
            if wP == l[-1]:
                s = s +'  '+ wP[0]+' '+ wP[1]
            else:
                s = s+ '  '+wP[0]+' '+ wP[1] + '\n'
    else:
        for wP in l[:5]:
            s = s +'  '+ wP[0]+' '+ wP[1] +'\n'
        s = s+ '  ...\n'
        for wP in l[-5:]:
            if wP == l[-1]:
                s = s+ '  '+wP[0]+' '+ wP[1]
            else:
                s = s+ '  '+wP[0]+' '+ wP[1] + '\n'
    return s
#using jaccard similarity it comapres word length similarity between different text
#d1 and d2 are dictionaries of sets of words of certain lengths
#the key for each set is length of the words we are comparing to find the similarity
def compareLenW(d1,d2):
    s = ''
    for words in range(1,max(len(d1),len(d2))+1):
        cLW = 0
        w1 = min(len(d1),words)
        w2 = min(len(d2),words)
        if len(d1[w1] | d2[w2]) != 0:
            cLW = len(d1[w1] & d2[w2])/len(d1[w1] | d2[w2])
        if words == max(len(d1),len(d2)):
            s = s + '{:4}: {:4.4f}'.format(words,cLW)
        else:
            s = s + '{:4}: {:4.4f}\n'.format(words,cLW)
    return s
#this code takes two text files and analyzes the words in them 
if __name__ == "__main__":
    fFile = input('Enter the first file to analyze and compare ==> ')
    print(fFile)
    sFile = input('Enter the second file to analyze and compare ==> ')
    print(sFile)
    mSep = int(input('Enter the maximum separation between words in a pair ==> '))
    print(mSep)
    #changes the files given into a lists of words
    l1 = splitTostr(textToString(fFile))
    l2 = splitTostr(textToString(sFile))
    #creates list of words that are redundant 
    stopWords = splitTostr(textToString('stop.txt'))
    #removes the redundant wordds from the list
    l1noStop = [item for item in l1 if item not in stopWords]
    l2noStop = [item for item in l2 if item not in stopWords]
    #gets average world length
    avgWlen1 = getAvgWordLen(l1noStop)
    avgWlen2 = getAvgWordLen(l2noStop)
    #finds ratio of distinct words to total words
    distinctW1 = distinctToTotal(l1noStop)
    distinctW2 = distinctToTotal(l2noStop)
    #creates dictionaries of sets of words based on their length
    lW1 = lenofWords(l1noStop)
    lW2 = lenofWords(l2noStop)
    #turns the dictionaries above into strings so the information can be easily digested
    wLSorted1 = wordsSorted(lW1)
    wLSorted2 = wordsSorted(lW2)
    #finds the distinct word pairs
    dWP1 = distinctWordPairs(l1noStop,mSep)
    dWP2 = distinctWordPairs(l2noStop,mSep)
    #finds jaccard similarity in word use 
    jSim = len((set(l1noStop) & set(l2noStop)))/len((set(l1noStop) | set(l2noStop)))
    #finds jaccard similarity in pairs of distinct and total word pairs
    dWordJ = len(set(dWP1[0]) & set(dWP2[0]) )/len(set(dWP1[0]) | set(dWP2[0]))
    #presents all the information above
    print()
    print('Evaluating document', fFile)
    print('1. Average word length: {:.2f}'.format(avgWlen1))
    print('2. Ratio of distinct words to total words: {:.3f}'.format(distinctW1))
    print('3. Word sets for document {}:'.format(fFile))
    print(wLSorted1)
    print('4. Word pairs for document {}'.format(fFile))
    print('  {} distinct pairs'.format(len(dWP1[0])))
    print(pairsF5L5(dWP1[0]))
    #ratio of distinct word pairs to total is calculated when printed
    print('5. Ratio of distinct word pairs to total: {:4.3f}'.format((len(dWP1[0])/len(dWP1[1]))))
    print()
    print('Evaluating document', sFile)
    print('1. Average word length: {:4.2f}'.format(avgWlen2))
    print('2. Ratio of distinct words to total words: {:4.3f}'.format(distinctW2))
    print('3. Word sets for document {}:'.format(sFile))
    print(wLSorted2)
    print('4. Word pairs for document {}'.format(sFile))
    print('  {} distinct pairs'.format(len(dWP2[0])))
    print(pairsF5L5(dWP2[0]))
    #ratio of distinct word pairs to total is calculated when printed
    print('5. Ratio of distinct word pairs to total: {:4.3f}'.format((len(dWP2[0])/len(dWP2[1]))))
    print()
    print('Summary comparison')
    if avgWlen1 > avgWlen2:
        print('1. {} on average uses longer words than {}'.format(fFile,sFile))
    else:
        print('1. {} on average uses longer words than {}'.format(sFile,fFile))
    print('2. Overall word use similarity: {:4.3f}'.format(jSim))
    print('3. Word use similarity by length:')
    print(compareLenW(lW1,lW2))
    print('4. Word pair similarity: {:4.4f}'.format(dWordJ))