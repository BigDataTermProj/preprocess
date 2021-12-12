import nltk

nltk.download([
     "names",
     "stopwords",
     "state_union",
    "twitter_samples",
     "movie_reviews",
     "averaged_perceptron_tagger",
     "vader_lexicon",
     "punkt",
 ])
 
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

for i in result:
  sia.polarity_scores(i)
  print(sia.polarity_scores(i))
