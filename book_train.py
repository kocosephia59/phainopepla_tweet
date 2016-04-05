import os
from process import *

#model = gensim.models.Word2Vec.load('moby_dick')

file_name=[]
for file in os.listdir("books/"):
    if file.endswith(".txt"):
        file_name.append(file)
        print(file)
        
print file_name

ctr=0
for f in file_name:
     hi='books/'+f
     print hi
     sentence = processfile(hi)
     
     print 'data_processed'
     if ctr == 0:
        model = gensim.models.Word2Vec(sentence, min_count=1, size=300)
     ctr += 1
     model.train(sentence)
     model.save("new_train")
    
#model.accuracy('questions-words.txt')    