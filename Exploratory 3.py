import re
fh = open('onlinebook.txt','r') #Opening the file
onlineFile = fh.read() #Reading all the content of the file
def wordsearch (onlinebook):
    if type(onlinebook) != str:
        raise TypeError("This is not a string")
# matches is to find all the words ending in at in the whole book
    Matches = re.findall(r"\w*at\b", onlineFile)
    for onlinebook in Matches:
        if len(onlinebook) > 3:
            L.append(onlinebook)
    #result = filter(lambda x: len(x)>=3, Matches)
    #return list(result)
    print L  #it will return all the words end with at and have length greater than equal to 3.

#fh = open('The Project Gutenberg eBook of Through Hell with Hiprah Hunt, by Arthur Young.','r') #Opening the file
#onlineFile = fh.read() #Reading all the content of the file
wordsearch(onlineFile) # Calling our function
