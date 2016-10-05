"""
distribution.py
Author: Liam A
Credit: http://stackoverflow.com/questions/16060899/alphabet-range-python,
http://stackoverflow.com/questions/1712227/how-to-get-the-size-of-a-list
http://stackoverflow.com/questions/6454894/reference-an-element-in-a-list-of-tuples
http://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.
Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:
* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.

(for me):  whooaa wah whohoho yeah well I got abbacedaga you just have a family cause moolaakayrassa quack!
"""

import string
txt=input("Please enter a string of text (the bigger the better): ")
txt2='"'+str(txt)+'"'
print('The distribution of characters in '+txt2+' is:')
appear = []
wappee = []

def compare(a, b):
    if b[1]<a[1]: #comparing numerical 2nd values in each tuple
        return True
    else:
        if b[0]>a[0]: #comparing string 1st values in each tuple
            return True
        else:
            return False

def bsort(seq, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it
txt=txt.lower()


alphabet=list(string.ascii_lowercase) #list of lowercase letters
for vy in range (0,26):
    nm=txt.count(alphabet[vy]) #finds the number of times a letter is in the string
    if nm!=0: #if the letter's in the string-
        appear.append(nm) #it notes the number of times the letter appears
        wappee.append(alphabet[vy]) #and what that letter is
whiir=int(len(appear)) #number of entries in the list "appear"

tupps = zip((list(wappee)),(list(appear))) #list of tuples, which displays a letter, and however many time a letter appears, if that letter appears at all
Ltup = list(tupps) #an actual list of the tuples
print(Ltup)
#nLtup = sorted(sorted(Ltup, key = lambda x : x[1]), key = lambda x : x[0], reverse = False)  #Ltup sorted

bsort(Ltup, compare)
#Ltup.sort(reverse=True) #sorts the list of tuples alphabetically
print(nLtup)
    
#print(' ')
for s in range(0,whiir):
    for duck in range(0,nLtup[s][1]):
        print(nLtup[s][0],end='')
    print(' ')
