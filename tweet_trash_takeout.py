import re, timeit, string
import nltk
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from string import maketrans

in_file= open('alltweets.txt', 'r')

new_file= open('cleantweets.txt', 'w')
links='http'
for line in in_file:
    
    if len(line.split()) > 3:
        if line.find(links)==-1:
            new_file.write(line)
    
    templine=line
        
in_file.close()
new_file.close()
