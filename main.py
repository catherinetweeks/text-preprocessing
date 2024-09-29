import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

url = input('Paste URL Here:')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#Extracting main text from specific html tag 
article_text = soup.find('div', class_='article-body').get_text()

#Tokenization into sentences
sentences = sent_tokenize(article_text)
#Tokenization into words
words = word_tokenize(article_text)
words = [word.lower() for word in words if word.isalpha()]
print(words)
