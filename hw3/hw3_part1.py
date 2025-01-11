from syllables import *
hardWords=[]
#Function splits string into sentences and puts it into a list of sentences
def splitStrToListOfSent(s):
    last=0
    sentences = []
    #iterates through the string and splits the string based on where the was sentencing ending punctuation
    for x in range(len(s)):
        if s[x]=='.' or s[x]=='?' or s[x]=='!':
            sentences.append(s[last:x])
            last=x+1
    return sentences
#calculates the average length of a sentence based off how many words it has
def avgSentenceLength(sentences):
    if type(sentences) == str:
        sentences=splitStrToListOfSent(sentences)
    total=0
    for z in sentences:
        sentence=z.split()
        total+=len(sentence)
    avg=total/len(sentences)
    return avg
#finds hard words based on a given string
#hard words are defined as having 3 or more syllables not having a dash or ending in es
def findHardWords(s):
    hard=[]
    s=s.split()
    for x in s:
        if find_num_syllables(x)>=3 and x.count('-')==0 and not x.find('es')==len(x)-2 and x not in hard:
                hard.append(x)
    return hard
#counts the number of total syablles in string and in this case a paragrpah
def syllablesP(p):
    count=0
    for x in p:
        count+=find_num_syllables(x)
    return count
if __name__ == "__main__":
    #ask user to enter paragraph to anaylze
    paragraph = input('Enter a paragraph => ')
    print(paragraph)
    pList=paragraph.split()
    #Average sentence length
    Asl=avgSentenceLength(paragraph)
    #finds hardwords
    hardWords=findHardWords(paragraph)
    #percentage of hardwords
    Phw=(len(hardWords)/len(pList))*100
    #Average number of syllables
    Asyl=syllablesP(pList)/len(pList)
    #readability measure
    Gfri=0.4*(Asl + Phw)
    #readability measure
    Fkri= 206.835-1.015*Asl-86.4*Asyl
    #Prints out information collected from the paragraph
    print('Here are the hard words in this paragraph:')
    print(hardWords)
    print('Statistics: ASL:{0:.2f} PHW:{1:.2f}% ASYL:{2:.2f}'.format(Asl,Phw,Asyl))
    print('Readability index (GFRI): {:.2f}'.format(Gfri))
    print('Readability index (FKRI): {:.2f}'.format(Fkri))
