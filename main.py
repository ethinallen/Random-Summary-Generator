import random
import string

def makeResponse():
    with open ('dictionary.txt','r') as f:
        data = f.readlines()
    #how many words you tryna cop?
    try:
        numWords = int(input('How many numbers do you want?'))
    except:
        print('You didn\'t enter a number')

    # creates our random string
    outputString = ''

    #inserts a period
    insPeriod = None

    #starts a new line
    newline = True

    # adds a new word to the random string for i number of words
    for i in range(numWords):
        newWord = data[random.randint(0,len(data) -1 )]
        newLen = int(len(newWord)-1)
        newWord = newWord[0:newLen]
        if newline == True:
            #capitalize the word that begins a new sentence
            newWord = string.capwords(newWord)
            newline = 0
        if insPeriod == 13:
            outputString += newWord
            outputString += '.' + ' '
            newline = 1
        else:
            outputString += newWord + ' '
            string.capwords(outputString)
        # average sentence contains 15 words but I am the chiefton of this reserve
        insPeriod = random.randint(0,13)
    print(outputString)

if __name__ == "__main__":
    makeResponse()
