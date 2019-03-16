# ECE143 Project Team 16 - Republican Candidate Tweets

## Members
* Jared	Johann Leitner
* Haonan Song
* Yuchen Tang
* Louise Xu

## Data Gathering Tools
* Tweepy (https://github.com/tweepy/tweepy)
    * Python Twitter API wrapper
    * Limited to last 3200 tweets
    * Requires authentication/developer account
* GetOldTweets-Python (https://github.com/Jefferson-Henrique/GetOldTweets-python)
    * Uses “Advanced Search” feature on Twitter to retrieve tweets
    * Authentication not required, but takes a longer amount of time
* Politician Tweets (https://data.world/bkey/politician-tweets)
    * Tweets by US politicians, congress people, senators and governors

## Repo Contents
* get_candidate_tweets.ipynb
    * Note: In order to use Tweepy, you will need to register for a Developer Twitter account (https://developer.twitter.com/)
* metric_visualization.ipynb
    * histograms
    * scatter plots
    * time series plots
* ratio_plot.ipynb
* sentiment_extraction.ipynb
* word_clouds.ipynb
