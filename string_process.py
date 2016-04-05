import re, timeit, string
import nltk
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from string import maketrans

#capital=r"A-Z"


def split_words(s):
    intab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outtab = "abcdefghijklmnopqrstuvwxyz"
    trantab = maketrans(intab, outtab)

    s=s.translate(trantab)

    table = string.maketrans("","")
    s=s.translate(table, string.punctuation)

#    print s
#    print s.split()
    return s.split()
#test=''.join([x.lower() for x in test])

test="Hello, World"
print split_words(test)
print split_words("Cory!, Come #heRe**\(*")

in_file= open('cleantweets.txt', 'r')
text = in_file.read()
sents = nltk.sent_tokenize(text)
print len(sents)
sentence=[]
for s in sents:
    
    sentence.append(split_words(s))
    
print sents[10]
print sentence[10]
print sents[len(sents)-1]
print sentence[len(sents)-1]

model = gensim.models.Word2Vec(sentence, min_count=1)
model.accuracy('questions-words.txt')

in_file.close()

model.save('twitter_model_1')