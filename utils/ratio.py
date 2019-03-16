import pandas as pd
def cal_ratio(fname):
    """
        calculate the ratio of the total favourite count to total retweet count during the primary time(1/2/2016-7/6/2016)
        :param: fname
        :type: str
        """
    assert isinstance(fname,str)
    assert fname!=[]
    lines=pd.read_csv(fname,error_bad_lines=False)
    start=0
    end=0
    for i in range(len(lines)):
        if lines.loc[i].date=="1/2/2016":
            end=i
        elif lines.loc[i].date=="7/6/2016":
            start=i
    res=lines[start:end]['favorites'].sum()/lines[start:end]['retweets'].sum()
    return res
print(cal_ratio("JohnKasich_tweets.csv"))
print(cal_ratio("marcorubio_tweets.csv"))
print(cal_ratio("tedcruz_tweets.csv"))
print(cal_ratio("trump_tweets.csv"))
print(cal_ratio("JebBush_tweets.csv"))



"""
    calculate the ratio of the total favourite count to total retweet count of different US politician
    calculate the average ratio
    the format of the data is bad so there's many if statements to avoid missing data
"""
with open('pol_tweets.csv','r') as f:
    lines = f.readlines()
    cnt_fav={}
    cnt_re={}
    for i in range(1,len(lines)):
        l=len(lines[i].split(";"))
        if(l<=4):
            continue
        if str(lines[i].split(";")[1]).isdigit()==False:
            continue
        if str(lines[i].split(";")[l-3]).isdigit() and str(lines[i].split(";")[l-4]).isdigit() and int(lines[i].split(";")[l-3])<1000000 and int(lines[i].split(";")[l-4])<1000000 and int(lines[i].split(";")[l-3])!=0 and int(lines[i].split(";")[l-4])!=0:
            if(lines[i].split(";")[1] in cnt_fav):
                k=lines[i].split(";")[1]
                cnt_fav[k]+=int(lines[i].split(";")[l-3])
                cnt_re[k]+=int(lines[i].split(";")[l-4])
            else:
                cnt_fav[lines[i].split(";")[1]]=0
                cnt_re[lines[i].split(";")[1]]=0
for i in list(cnt_fav.keys()):
    if cnt_fav[i]<1000 or cnt_re[i]<1000:
        del cnt_fav[i]
        del cnt_re[i]
ratio={}
for i in list(cnt_fav.keys()):
    if(cnt_re[i]==0):
        continue
    ratio[i]=cnt_fav[i]/cnt_re[i]
res=sorted(list(ratio.values()))
res.append(cal_ratio("trump_tweets.csv"))
res.sort()
average=sum(cnt_fav.values())/sum(cnt_re.values())
print(average)
