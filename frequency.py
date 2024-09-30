from nltk.probability import FreqDist
from main import words_lower

frequency = FreqDist(words_lower)
#print the 5 most common words from the article. 
print(frequency.most_common(5))
