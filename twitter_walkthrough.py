import tweepy
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from nltk.sentiment.vader import SentimentIntensityAnalyzer

consumer_key = CONSUMER_KEY
consumer_secret = CONSUMER_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

driver=webdriver.Chrome(PATH_TO_CHROMEDRIVER)
driver.get('https://twitter.com/login')

#login
driver.find_element_by_class_name("js-username-field").send_keys(USERNAME)
driver.find_element_by_class_name('js-password-field').send_keys(PASSWORD)
driver.find_element_by_class_name("EdgeButtom--medium").click()
time.sleep(1)
        
search = UTILITY_COMPANY
numberOfUsers = 1

# find and respond to tweets
for tweet in tweepy.Cursor(api.search, search,lang='en').items(numberOfUsers):
    tweetId = tweet.user.id
    username = tweet.user.screen_name
    phrase = 'Ever thought about renewable energy? Check out my website'
    print (tweet.text)
    para = nltk.sent_tokenize(tweet.text) # this gives us a list of sentences

# now loop over each sentence and tokenize it separately
    for sentence in para:
        tokenized_para = nltk.word_tokenize(sentence)
        tags = nltk.pos_tag(tokenized_para)
        print(tags)
        tree = chunk.ne_chunk(tags)
        tree
        tree.draw()

#analyze sentiment in tweet
tool = SentimentIntensityAnalyzer()
for sentence in para:
    print(sentence)
    ss = tool.polarity_scores(sentence)
    for i in sorted(ss):
        print('{0}: {1}, '.format(i, ss[i]), end='') 
        if ss["compound"] < 0.0:
