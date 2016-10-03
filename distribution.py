"""
distribution.py
Author: Liam A
Credit: http://stackoverflow.com/questions/16060899/alphabet-range-python,
http://stackoverflow.com/questions/1712227/how-to-get-the-size-of-a-list
http://stackoverflow.com/questions/6454894/reference-an-element-in-a-list-of-tuples
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

whooaa wah whohoho yeah well I got abbacedaga you just have a family cause moolaakayrassa quack!
"""

import string
txt=input("Please enter a string of text (the bigger the better): ")
txt2='"'+str(txt)+'"'
print('The distribution of characters in '+txt2+' is:')
appear = []
wappee = []

"""
appear.append("b")
appear.append("c")
appear.append("a")
print(list(appear))
"""

alphabet=list(string.ascii_lowercase)
for vy in range (0,26):
    nm=txt.count(alphabet[vy])
    if nm!=0:
        appear.append(nm)
        wappee.append(alphabet[vy])
whiir=int(len(appear))

tupps = zip((list(appear)),(list(wappee)))
Ltup = list(tupps)
print(Ltup)
Ltup.sorted([none[none[true]]])
print(Ltup)

#print(' ')
for s in range(0,whiir):
    for duck in range(0,Ltup[s][0]):
        print(Ltup[s][1],end='')
    print(' ')

