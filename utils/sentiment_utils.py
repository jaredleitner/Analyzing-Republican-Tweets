import pandas as pd
import string
from textblob import TextBlob # Used for text analysis


def get_sentiment_score(tweets):
    """
    Adds a sentiment score for each tweet in an additional column 
    
    Arguments:
    tweets (DataFrame): tweets DataFrame for certain individual
    
    Returns:
    tweets (DataFrame): updated DataFrame with sentiment score column
    """
    assert isinstance(tweets, pd.DataFrame)
    
    tweets['sentiment_polarity'] = 0

    for count, tweet in enumerate(tweets.text):
        tweet = tweet.translate(str.maketrans('', '', string.punctuation))
        tweet = " ".join(filter(lambda x:x[:5]!='https', tweet.split()))
        analysis = TextBlob( tweet )
        tweets.loc[count,'sentiment_polarity'] = analysis.sentiment.polarity

    return tweets
