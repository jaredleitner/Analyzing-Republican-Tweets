import pandas as pd
import string
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def remove_punctuation(tweets):
    """
    Removes punctiation and non-sensical characters from the tweets
    
    Arguments:
    tweets (str): string containing all tweets from certain candidate
    
    Returns:
    tweets (str): cleaned up string containing all tweets    
    """
    
    assert isinstance(tweets, str), "Must pass a string"
    
    tweets = " ".join(filter(lambda x:x[:5]!='https', tweets.split()))
    tweets = " ".join(filter(lambda x:x[0]!='@', tweets.split()))
    tweets = " ".join(filter(lambda x:x[:2]!='b"', tweets.split()))
    tweets = " ".join(filter(lambda x:x[:2]!="b\'", tweets.split()))
    tweets = tweets.translate(str.maketrans('', '', string.punctuation))
    tweets = " ".join(filter(lambda x:x[:4]!="bRT", tweets.split()))
    tweets = " ".join(filter(lambda x:x[:2]!="xe", tweets.split()))
    tweets = " ".join(filter(lambda x:x[:3]!="Ixe", tweets.split()))
    tweets = " ".join(filter(lambda x:x[0]!="â", tweets.split()))
    tweets = tweets.lower()
    
    return tweets


def make_word_cloud(tweets, stop_words, png_filename=None, image=None):
    """
    Creates a wordcloud for the given tweets DataFrame
    
    Arguments:
    tweets (DataFrame): tweets DataFrame of candidate
    stop_words (set): set of words to be excluded from making the wordcloud
    png_filename (str): file to save the wordcloud to - default is None
    image (np.array): image mask for creating wordcloud shape - default is None
    """
    assert isinstance(tweets, pd.DataFrame)
    assert isinstance(stop_words, set)
    if png_filename != None:
        assert isinstance(png_filename, str)
        assert png_filename[-4:] == '.png'

    tweet_list = ""
    for tweet in tweets.text:
        tweet_list += tweet
        tweet_list += " "
    
    tweet_list = remove_punctuation(tweet_list)
    
    # Generate a word cloud image
    wordcloud = WordCloud( background_color='white', mask=image, colormap='gist_heat',max_font_size=80,
                          stopwords=stop_words, contour_width=3,contour_color='black', collocations=False).generate(tweet_list)

    # Display the generated image:
    plt.figure(figsize=(8,12))
    plt.axis("off")
    plt.imshow(wordcloud,  interpolation='bilinear')
    if png_filename!=None:
        plt.savefig('WordClouds/{}'.format(png_filename))

    
