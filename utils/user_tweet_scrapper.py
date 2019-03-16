import tweepy #https://github.com/tweepy/tweepy
import csv

# Developer Twitter account credentials
import user_credentials as cred
consumer_key = cred.consumer_key
consumer_secret = cred.consumer_secret
access_key = cred.access_key
access_secret = cred.access_secret

# Authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#Modified from https://gist.github.com/yanofsky/5436496
#Twitter only allows access to a users most recent 3240 tweets with this method
def get_all_tweets(screen_name):
    """
    " Retrieve the most recent tweets of a user, up to their 3240th most recent tweet
    " For retrieving older tweets, consider using GetOldTweets-Python 
    " (https://github.com/Jefferson-Henrique/GetOldTweets-python)
    "
    " screen_name: screen name of the user whose tweets are to be retrieved
    """
    assert isinstance(screen_name, str)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []	
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        print("...%s tweets downloaded so far" % (len(alltweets)))

    #transform the tweepy tweets into a 2D array that will populate the csv	
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), 
                  tweet.favorite_count if hasattr(tweet, 'favorite_count') else "", 
                  tweet.retweet_count if hasattr(tweet, 'retweet_count') else "", 
                  tweet.reply_count if hasattr(tweet, 'reply_count') else "", 
                  tweet.quote_count if hasattr(tweet, 'quote_count') else ""] for tweet in alltweets]
    
    #write the csv
    with open('%s_tweets.csv' % screen_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['id','created_at','text','favorite_count','retweet_count','reply_count','quote_count'])
        writer.writerows(outtweets)

    return outtweets