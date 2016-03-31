
from nltk.stem.porter import PorterStemmer

f1 = open('/home/yinhao/scripts/fp_growth/positive.txt')
f2 = open('/home/yinhao/scripts/fp_growth/positive_post.txt','w+')

temp_lines = []
for line in f1.readlines():
    if line not in temp_lines:
        temp_lines.append(line)
f1.close()

stemmer = PorterStemmer()

for line in temp_lines:
    temp_words = []
    lines = line.strip().split(' ')
    for item in lines:
        word = stemmer.stem(item)
        if word not in temp_words and len(word) > 1:
            temp_words.append(word)
    temp_words.append('\n')
    for word in temp_words:
            f2.write(word)
            f2.write(' ')
f2.close()

