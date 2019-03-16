import collections
import operator
import copy
import pandas as pd
import string
from textblob import TextBlob 
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np

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


def n_gram(tweets, n, stop_words):
    """
    Produces an list of highest frequency N-grams along with their count
    
    Arguments:
    tweets (DataFrame): tweets DataFrame for a certain candidate
    n (int): number of words for n gram    
    stop_words (set): set of words that are not used for making the N-gram
    
    Returns:
    max_grams (list): list of highest frequency N-grams
    """
    
    assert isinstance(tweets, pd.DataFrame)
    assert isinstance(n, int)
    assert isinstance(stop_words, set)

    tweet_list = ""
    for tweet in tweets.loc[:,'text']:
        tweet_list += tweet
        tweet_list += " "
        
    tweet_list = remove_punctuation(tweet_list)
    tweets_analysis = TextBlob(tweet_list)
    
    grams = tweets_analysis.ngrams(n=n)
    
    gram_counter = collections.Counter()

    for words in grams:
        words_list = list(words)
        word = " ".join(words_list)
        gram_counter[word] += 1
        
    gram_dict = dict(gram_counter)

    num_grams = 100
    max_grams_list = []

    for i in range(num_grams):
        current_max = max(gram_dict.items(), key=operator.itemgetter(1))
        max_grams_list.append(current_max)
        del gram_dict[current_max[0]]
        
    max_grams = copy.deepcopy(max_grams_list)

    for gram in max_grams_list:
        words = gram[0].split(" ")
        for word in words:
            if word in stop_words and gram in max_grams:
                max_grams.remove(gram)

    return max_grams


def plot_ngrams(max_grams, ngram_number):
    """
    Contructs a bar graph for the top 5 N-grams 
    
    Arguments:
    max_grams (list): list of tuples, where each tuple contains an N-gram and the corresponding count
    ngram_number (int): N-gram number
    """
    assert isinstance(max_grams, list)
    assert len(max_grams) >= 5
    assert isinstance(ngram_number, int)
    
    fig, ax = plt.subplots()

    ind = np.arange(5)    # the x locations for the groups
    width = 0.5       # the width of the bars

    counts = [max_grams[0][1], max_grams[1][1], max_grams[2][1], max_grams[3][1], max_grams[4][1]]
    p1 = ax.bar(ind, counts, width=width, color=['black', 'red', 'green', 'blue', 'cyan'], align='edge')

    ax.set_title('{}-Grams'.format(ngram_number))
    ax.set_xticks(ind + width / 2)
    
    if ngram_number == 1:
        x_labels = [gram[0] for gram in max_grams]

    if ngram_number == 2:
        x_labels = [gram[0].split(" ")[0] + "\n" + gram[0].split(" ")[1] for gram in max_grams]

    if ngram_number == 3:
        x_labels = [gram[0].split(" ")[0] + "\n" + gram[0].split(" ")[1] + "\n" + gram[0].split(" ")[2] for gram in max_grams]

    ax.set_xticklabels(x_labels, fontdict={'fontsize': 13,
                                         'fontweight': 10})

    plt.ylabel("Count", size=14)
    plt.tight_layout()

    plt.show()




