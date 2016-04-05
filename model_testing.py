import re, timeit, string
import nltk
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from string import maketrans
from process import split_words

test_model = gensim.models.Word2Vec.load('new_train')

#test_model.accuracy('questions-words.txt') 

#similarities = test_model.most_similar(positive=['zombie'], negative=[], topn=10)
#for item in similarities:
#    print item[0],"     ",item[1]


def sim_pos_neg(positives,negatives):
    more_sim= test_model.most_similar(positive=positives, negative=negatives, topn=10)
    for item in more_sim:
        print item[0],"     ",item[1]
    print '\n'    
    return

def sim_two(first,second):
    more_sim= test_model.most_similar(positive=[first], negative=[second], topn=10)
    for item in more_sim:
        print item[0],"     ",item[1]
    print '\n'    
    return

def similar(word):
    more_sim= test_model.most_similar(positive=[word], negative=[], topn=1)
    item = more_sim[0]
    return item


#sim_two('whale','moby')
#sim_two('woman', 'pip')
#sim_pos_neg(['woman','king'],['man'])
#sim_pos_neg(['father','woman'],['man'])
#sim_pos_neg(['son','girl'],['boy'])
#sim_pos_neg(['family','bat'],['parents'])
sim_pos_neg(['star','wars'],[])

tweetfile=open('books/cleantweets.txt','r')
ctr=0
for tweet in tweetfile:
    text = split_words(tweet)
    repstr = ""
    try:
        for word in text:
            item = similar(word)
            if item[1] > 0.5:
                repstr += item[0]
                repstr += ' '
            else:
                repstr += word +' '
        #print "ORIGINAL:     ", tweet
        #print "REPLACED:     ", repstr
        #print "---------------------------------------------"
    except:
        ctr += 1