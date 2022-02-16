uniquewords=[]
def findUnique(word):
    for w in uniquewords:
        return False
    uniquewords.append(word)
    return True

def removeduplicates(msg):
    newmsg=""
    word=""
    i=0
    while i<len(msg):
        if msg[i]==" ":
            if findUnique(word):
                newmsg=newmsg+word+" "
            word=""
        else:
            word=word+msg[i]
        i=i+1
    if findUnique(word):
        newmsg=newmsg+word
    print(newmsg)
removeduplicates("hello hi hello hi shafeeq shafeeq hi")