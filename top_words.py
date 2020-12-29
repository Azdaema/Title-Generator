import sys
import string
import re
import unicodedata
from collections import Counter 

def topWords(stringIn):
    # Remove punctuation
    stringIn = "".join(l for l in stringIn if l not in "!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~")
    
    # split() returns list of all the words in the string 
    words = stringIn.split()
      
    # Pass the words list to instance of Counter class. 
    c = Counter(words)
    
    ignore = [
        #articles
        'a','an','the',
        #pronouns
        'i','me','my','mine','you','your','yours','we','our','ours','it','its','he','him','his','she','her','hers','they','them','their','theirs',
        'that','this','here','there','what',
        #prepositions
        'in', 'at', 'on', 'of', 'to','for','with','than',
        #conjunctions
        'and','but','or','so','as','if','by','not','like','into',
        #misc
        'be','been','was','is','had','did','were','would','could','will','do','have','too'
        ]
    for word in list(c):
        if word.lower() in ignore:
            del c[word]
        if re.search('\'d$', word) or re.search('\'ve$', word) or re.search('\'ll$', word) or re.search('\'s$', word):
            del c[word]
    return c
    
fic_text = ""
for line in sys.stdin:
    fic_text = fic_text + str(line.encode('utf-8').decode('ascii', 'ignore'))



words = topWords(fic_text)
for w, count in words.most_common(20):
        if count > 1:
             print '%d: %s' % (count, w)
             
