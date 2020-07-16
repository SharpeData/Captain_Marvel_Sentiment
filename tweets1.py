import pandas as pd 
import datetime as dt 
from twitterscraper import query_tweets
from langdetect import detect 

def detector(x):
    try:
       return detect(x)
    except:
        None 
        
begin_date = dt.date(2019,3,3)
end_date = dt.date(2019,3,7)

begin_date_premier = dt.date(2019,3,7)
end_date_premier = dt.date(2019,3,9)

tweets_before = query_tweets("#CaptainMarvel", begindate = begin_date, enddate= end_date, limit = 100000)

tweets_after = query_tweets("#CaptainMarvel", begindate = begin_date_premier, enddate = end_date_premier)
                            
df_before = pd.DataFrame(t.__dict__ for t in tweets_before)
df_after = pd.DataFrame(t.__dict__ for t in tweets_after)

#filter for english tweets
df_before['lang'] = df_before['text'].apply(lambda x:detector(x))
df_before = df_before[df_before['lang'] == 'en']
df_after['lang'] = df_after['text'].apply(lambda x: detector(x))
df_after = df_after[df_after['lang'] == 'en'] 

#save files
df_before.to_csv('cm_tweets_before_clean.csv')
df_after.to_csv('cm_tweets_after_clean.csv')
