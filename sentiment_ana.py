import string
from collections import Counter
import matplotlib.pyplot as plt

raw_text = open("read.txt", encoding='utf-8').read()

lower_text = raw_text.lower()

clean_text = lower_text.translate(str.maketrans('', '', string.punctuation))

tokenized = clean_text.split()

# print(tokenized)


stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
word_list = []
for token in tokenized:
    if token not in stop_words:
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
plt.savefig('pie.png')
plt.show()
