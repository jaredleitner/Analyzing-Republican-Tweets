import pandas as pd
def getAverageSentiment(dataframe):
    '''
    Get the average sentiment for candidates 
    Input:
        dataframe
    Type:
        pandas.core.frame.DataFrame
    Return:
        average sentiment score
    Type:
        float
    '''
    assert isinstance(dataframe,pd.core.frame.DataFrame),'the input file is not pandas dataFrame type'
    
    total_sentiment = 0
    numOfTweets = 0
    for idx,row in dataframe[['sentiment_polarity']].iterrows():
        total_sentiment += row[0]
        numOfTweets += 1
    return total_sentiment/numOfTweets




def getNumOfExtremeSentiment(dataframe):
    '''
    Get the number of +1.0 and -1.0 sentiment polarity tweets from giving dataframe and their IDs
    Input:
        dataframe
    Type:
        pandas.core.frame.DataFrame
    Return:
        dictionary with number of tweets and the list contains IDs as value.
    Type:
        dict
    '''
    assert isinstance(dataframe,pd.core.frame.DataFrame),'the input file is not pandas dataFrame type'
    
    num_Pos1sentiment = 0 
    num_Neg1sentiment = 0
    idx_Pos = []
    idx_Neg = []
    final_dict = {}
    for idx,row in dataframe[['sentiment_polarity']].iterrows():
        if row[0] == 1.0:
            num_Pos1sentiment +=1
            idx_Pos.append(idx)
        elif row[0] == -1.0:
            num_Neg1sentiment +=1
            idx_Neg.append(idx)
    final_dict = {'the number of +1.0 polarity tweets is': num_Pos1sentiment,
                 'the IDs of +1.0 polarity tweets are': idx_Pos,
                 'the number of -1.0 polarity tweets is': num_Neg1sentiment,
                 'the IDs of -1.0 polartiy tweets are': idx_Neg}    
    return final_dict

