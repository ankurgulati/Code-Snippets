
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:52:23 2017

@author: ankur
"""

import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
#nltk.download("stopwords")

cache_english_stopwords=stopwords.words('english')



def tweet_clean(tweet):
    # Remove tickers
    sent_no_tickers=re.sub(r'\$\w*','',tweet)
    #Tokenizer
    tw_tknzr=TweetTokenizer(strip_handles=True, reduce_len=True) 
    temp_tw_list = tw_tknzr.tokenize(sent_no_tickers)
    # Remove stopwords
    list_no_stopwords=[i for i in temp_tw_list if i.lower() not in cache_english_stopwords]
    # Remove hyperlinks
    list_no_hyperlinks=[re.sub(r'https?:\/\/.*\/\w*','',i) for i in list_no_stopwords]
    # Remove hashtags
    list_no_hashtags=[re.sub(r'#', '', i) for i in list_no_hyperlinks]
    # Remove Punctuation and split 's, 't, 've with a space for filter
    list_no_punctuation=[re.sub(r'['+string.punctuation+']+', ' ', i) for i in list_no_hashtags]
    # Remove multiple whitespace
    new_sent = ' '.join(list_no_punctuation)
    # Remove any words with 2 or fewer letters
    filtered_list = tw_tknzr.tokenize(new_sent)
    list_filtered = [re.sub(r'^\w\w?$', '', i) for i in filtered_list]
    filtered_sent =' '.join(list_filtered)
    clean_sent=re.sub(r'\s\s+', ' ', filtered_sent)
    #Remove any whitespace at the front of the sentence
    clean_sent=clean_sent.lstrip(' ')
    print('Clean sentence:')
    print(clean_sent)

s0='    RT @Amila #Test\nTom\'s newly listed Co. &amp; Mary\'s unlisted     Group to supply tech for nlTK.\nh.. $TSLA $AAPL https:// t.co/x34afsfQsh'
tweet_clean(s0)
