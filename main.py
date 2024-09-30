import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

url = str(input('Paste URL Here:'))
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#Extracting main text from specific html tag 
article_text = soup.find('div', class_='article-body').get_text()

#Tokenization into sentences
words = word_tokenize(article_text)

#Making one list where all words are lowercase
words_lower = [word.lower() for word in words if word.isalpha()]

#Removing stop words
stops = set(stopwords.words('english'))
words_lower = [word for word in words_lower if word not in stops]
words = [word for word in words if word not in stops]

#Reducing words to their root form (ie running -> run)
lemmatizer = WordNetLemmatizer()
words_lower = [lemmatizer.lemmatize(word) for word in words_lower]
words = [lemmatizer.lemmatize(word) for word in words]
