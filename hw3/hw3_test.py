def splitStrToListOfSent(s):
    last=0
    sentences = []
    for x in range(len(s)):
        if s[x]=='.' or s[x]=='?' or s[x]=='!':
            sentences.append(s[last:x])
            last=x+1
    return sentences
def avgSentenceLength(sentences):
    total=0
    print(len(sentences))
    for z in sentences:
        sentence=z.split()
        total+=len(sentence)
    avg=total/len(sentences)
    return avg
slay=splitStrToListOfSent('WOW jacky cen. slay christopher gee. poggers ! ILOVEMYGF  !')
print(avgSentenceLength(slay))