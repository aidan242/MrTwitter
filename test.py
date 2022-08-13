import twitter_api
import markov_tweet
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ['API_KEY']
api_key_secret = os.environ['API_KEY_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

t_api = twitter_api.TwitterApi(api_key,api_key_secret,access_token,access_token_secret)
trends = t_api.get_trends()
hashtags = t_api.extract_hashtags(trends)
print(f'HASHTAGS: {hashtags}\n\n')


init_tweets = t_api.get_n_tweets(hashtags[0], 500)
m_tweeter = markov_tweet.MarkovTweet(hashtags[0], init_tweets)
m_tweeter.create_model()
print(f'TWEET TEXT FOR: {hashtags[0]}\n{m_tweeter.create_tweet_long()}\n\n')
print(f'TWEET TEXT FOR: {hashtags[0]}\n{m_tweeter.create_tweet_long()}\n\n')
print(f'TWEET TEXT FOR: {hashtags[0]}\n{m_tweeter.create_tweet_long()}\n\n')
print(f'TWEET TEXT FOR: {hashtags[0]}\n{m_tweeter.create_tweet_long()}\n\n')
print(f'TWEET TEXT FOR: {hashtags[0]}\n{m_tweeter.create_tweet_long()}\n\n')

# for hashtag in hashtags:
#     init_tweets = t_api.get_n_tweets(hashtag, 100)
#     m_tweeter = markov_tweet.MarkovTweet(hashtag, init_tweets)
#     m_tweeter.create_model()
#     print(f'TWEET TEXT FOR: {hashtag}\n{m_tweeter.create_tweet()}\n\n')