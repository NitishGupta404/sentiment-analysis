import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

raw_text = open("read.txt", encoding='utf-8').read()

lower_text = raw_text.lower()

clean_text = lower_text.translate(str.maketrans('', '', string.punctuation))

tokenized=word_tokenize(clean_text ,'english')

word_list = []
for token in tokenized:
    if token not in stopwords.words("english"):
        word_list.append(token)


print(word_list)

emotion_list = []

with open("emotions.txt", 'r') as file:
    for line in file:
        clean_line = line.replace("\n", '').replace(',', '').replace("'", '').strip()
        word, emotion = clean_line.split(':')
        if word in word_list:
            emotion_list.append(emotion)

emotion_count = Counter(emotion_list)

print(emotion_count)

fig, axl=plt.subplots()
axl.bar(emotion_count.keys(), emotion_count.values())
fig.autofmt_xdate()
plt.savefig('bar.png')
plt.show()