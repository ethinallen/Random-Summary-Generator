import random
import string

def makeResponse():
    with open ('/Users/Desktop/dictionary.txt','r') as f:
        data = f.readlines()
    #how many words you tryna cop?
    numWords = 100
    
    #initiate random string
    REEEEE = ''
    
    #inserts a period
    insPeriod = False
    
    #starts a new line
    newline = True
    for i in range(numWords):
        lengthString = random.randint(1,6)
        newWord = data[startPos]
        newLen = int(len(newWord)-1)
        newWord = newWord[0:newLen]
        if newline == True:
            #capitalize the word that begins a new sentence 
            newWord = string.capwords(newWord)
            newline = 0
        if insPeriod == 13:
            REEEEE = REEEEE + newWord
            REEEEE = REEEEE + '.' + ' '
            newline = 1
        else:
            REEEEE = REEEEE + newWord + ' '
            string.capwords(REEEEE)
        # average sentence contains 15 words but I am the chiefton of this reserve
        insPeriod = random.randint(0,13)
    print(REEEEE)

if __name__ == "__main__":
    makeResponse()
