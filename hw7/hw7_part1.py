'''
code takes a dictionary, list of input words and words similar to other letters and then tries to autocorrect them based off the dictionary
Randy Taylor
'''
#file name
def createListOfWord(f):
    l = []
    for line in open(f):
    #strips the new line part and a space because some inputs have a space
        l.append(line.strip('\n').strip())
    #add each line to the file
    return l
#file name
def createDict(f):
    d = dict()
    #for every line in the file we split it up into the word and lexiographic number
    #next we use our dictionary above to make the word the key and the number the value 
    #returns the created dictionary
    for line in open(f):
        l = line.split(',')
        d[l[0]] = l[1].strip('\n')
    return d
#takes a dictionary and word that is a string as inputs
#the word is in the dictionary return True if it is not then we return False
def foundinDict(d,w):
    if w in d:
            return True
    return False
#drop letter
#dictionary and word
def dropL(d,w):
    #potentialWords
    pW = set()
    #tries dropping a letter for every word in the word given
    #if that word is found in the dictionary we add it to a set of potential words
    for l in range(len(w)):
        word = w[:l] + w[l+1:]
        if foundinDict(d,word):
            pW.add(word)
    return pW
#insert letter
#dictionary, word
def insertL(d,w):
    #potential words
    pW = set()
    #creates a list of every letter in the alphabet
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    w = list(w)
    #tries inserting every letter in the alphabet at each point in the word to see if it is a word
    #converts w to a list so that the insert function can be used 
    for l in range(len(w)+1):
        for a in alphabet:
            word = w.copy()
            word.insert(l,a)
            word = ''.join(word)
            if foundinDict(d,word):
                pW.add(word)
    return pW
#swap letter
#dictionary, word
def swapL(d,w):
    #potential words
    pW = set()
    w = list(w)
    #swaps every letter till the end in the given word and if is in the dictionary adds it to potential words
    for l in range(len(w)-1):
        word = w.copy()
        word[l],word[l+1] = word[l+1],word[l]
        word = ''.join(word)
        if foundinDict(d,word):
            pW.add(''.join(word))
    return pW
#takes each line in the keyboard file and uses that to make a list of common replacements for letters
def splitKey(d):
    kL = dict()
    for line in open(d):
        l = line.strip().split()
        kL[l[0]] = l[1:]
    return kL
#replace letter
#takes a dictionary, word, keyboard
def repL(d,w,k):
    #potential words
    pW = set()
    #replaces letters with common replacements from keyboard and if they exist adds them to potential words
    for l in range(len(w)):
        for let in k[w[l]]:
            word = w[:l] + let + w[l+1:]
            if foundinDict(d,word):
                 pW.add(word)
    return pW
#sorts lexiographically
#takes a given set and dictionary
#based off the words from the set it sorts the words from most common usage using the lexiographic number found in the dictionary from greatest to least
#returns the first three words
def sortLex(s,d):
    lt = []
    for w in s:
        lt.append((d[w],w))
    lt.sort(reverse = True)
    words = []
    for w in lt:
        words.append(w[1])
    return words[0:3]
if __name__ == "__main__":
    #gets dictionary file
    dictFile = input('Dictionary file => ').strip()
    print(dictFile) 
    #gets input words file
    inFile = input('Input file => ').strip()
    print(inFile)
    #gets keyboard file
    keyFile = input('Keyboard file => ').strip()
    print(keyFile)
    #list of words
    lOW = createListOfWord(inFile)
    #dictionary
    d =createDict(dictFile)
    #keyboard split 
    k = splitKey(keyFile)
    #prints out facts about the words based on the functions above
    for w in lOW:
       all = dropL(d,w) | insertL(d,w) | swapL(d,w) | repL(d,w,k)  
       if foundinDict(d,w):
           print('{:>15} -> FOUND'.format(w))
       else:
            if len(all) == 0:
                print('{:>15} -> NOT FOUND'.format(w))
            else:
                print('{:>15} -> FOUND{:>3}:  {}'.format(w,len(all),' '.join(sortLex(all,d))))
   