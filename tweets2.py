import pandas as pd 
import datetime as dt 
from twitterscraper import query_tweets
from langdetect import detect 

def detector(x):
    try:
       return detect(x)
    except:
        None 
        
begin_date_a = dt.date(2018,4,23)
end_date_a = dt.date(2018,4,27)

begin_date_premier_a = dt.date(2018,4,28)
end_date_premier_a = dt.date(2018,4,30)

a_tweets_before = query_tweets("#Avengers OR #InfinityWar", begindate = begin_date_a, enddate= end_date_a, limit = 200000)
a_tweets_after = query_tweets("#Avengers OR #InfinityWar", begindate = begin_date_premier_a, enddate = end_date_premier_a, limit = 200000)
                            
a_df_before = pd.DataFrame(t.__dict__ for t in a_tweets_before)
a_df_after = pd.DataFrame(t.__dict__ for t in a_tweets_after)

#filter for english tweets
a_df_before['lang'] = a_df_before['text'].apply(lambda x:detector(x))
a_df_before = a_df_before[a_df_before['lang'] == 'en']
a_df_after['lang'] = a_df_after['text'].apply(lambda x: detector(x))
a_df_after = a_df_after[a_df_after['lang'] == 'en']

#save files
a_df_before.to_csv('avengers_tweets_before_clean.csv')
a_df_after.to_csv('avengers_tweets_after_clean.csv')
