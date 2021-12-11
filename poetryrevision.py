from google.colab import drive
drive.mount('/content/gdrive')

# imports
import random
import re
import nltk
nltk.download('punkt')

# open the file
with open("/content/gdrive/My Drive/In Cabin Ships at Sea2.txt") as f:
  text = f.read()

text = text.lower()
text = re.sub(r'[^\w\s]', '', text)
text = text.split()
text.reverse()

# pick a random word for the title
title = random.choice(text)

# print that title word in all caps
print("\n\n\n" + title.upper() + ", a poem. \n")

# get a list of sentences shorter than some specified length
short_sentences = []
c = 0
while c < 7:
  sentence = ""
  for x in range(6):
    sentence = sentence + text[x] + " "
  for x in range(6):
    text.pop(x)

  short_sentences.append(sentence)

  c = c + 1

for x in range(len(short_sentences)):
  print(short_sentences[x])
