
# coding: utf-8

# In[2]:


import random
import string

def makeResponse():
    with open ('/Users/andrewemery/Desktop/dictionary.txt','r') as f:
        data = f.readlines()
    #how many words you tryna cop?
    numWords = 100
    #I wanted to use base1 indexing but I'm not one of those dum enjineres (i am most certainly am)
    startPos = 0
    REEEEE = ''
    #should i insert a period? not yet you tricky boy, you
    insPeriod = False
    #do I want to start a new line RIGHT OFF THE BAT 
    #### YER DANG STRAIT I DO
    newline = True
    for i in range(numWords):
        lengthString = random.randint(1,6)
        startPos = random.randint(0,(len(data)-6))
        newWord = data[startPos]
        newLen = int(len(newWord)-1)
        newWord = newWord[0:newLen]
        if newline == True:
            newWord = string.capwords(newWord)
            newline = 0
        if insPeriod == 13:
            REEEEE = REEEEE + newWord
            REEEEE = REEEEE + '.' + ' '
            newline = 1
        else:
            REEEEE = REEEEE + newWord + ' '
            string.capwords(REEEEE)
        insPeriod = random.randint(0,13)
    print(REEEEE)

if __name__ == "__main__":
    makeResponse()
