#Stemmer
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk import PorterStemmer
from nltk import pos_tag
word="Dhoni is the captain of Indian cricket team. He is a great player."
tokens_stopwords=stopwords.words("english")
word_tokens=word_tokenize(word)
stemming = []

for word in tokens_stopwords:
    stemming.append(PorterStemmer().stem(word))
print(stemming)
#Lemmatizer
from nltk import WordNetLemmatizer
lma = []
for word in tokens_stopwords:
    lma.append(WordNetLemmatizer().lemmatize(word))
print(lma)
#POS Tags

print(pos_tag(word_tokens))