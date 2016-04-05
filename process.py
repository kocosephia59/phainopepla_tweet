import re, timeit, string
import nltk
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from string import maketrans

def split_words(s):
    intab = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outtab = "abcdefghijklmnopqrstuvwxyz"
    trantab = maketrans(intab, outtab)
    s=s.encode('utf-8')
    s=s.translate(trantab)

    #print len(s)
    table = string.maketrans("","")
    s=s.translate(table, string.punctuation)

    return s.split()

def processfile(filename):

    in_file= open(filename, 'r')
    text = in_file.read()
    sents = nltk.sent_tokenize(text.decode('utf8'))
    
    sentence=[]
    for s in sents:    
        sentence.append(split_words(s))

    in_file.close()
    return sentence
    
def model_train(sentence, model_name):
    model = gensim.models.Word2Vec(sentence, min_count=1, size=300)
#    model.accuracy('questions-words.txt')
    model.save(model_name)
    return 