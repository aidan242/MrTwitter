from operator import length_hint
import re
import math
import random
import markovify

"""Generate tweets using array of tweepy tweet objects using markov chain"""
class MarkovTweet:
    def __init__(self,hashtag,tweets) -> None:
        """
        :param hashtag: Hashtag for all tweets passed into object. String
        :param tweets: List of tweepy tweets.
        """
        self.hashtag = hashtag

        self.tweets = self.clean_tweets_str(tweets)
        self.tweet_length = math.floor( sum( map(len, self.tweets) ) / len(self.tweets) )
        self.model = self.create_model()

    def clean_tweets(self, tweets):
        clean_tweets = []
        format_regex = "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)"
        for tweet in tweets:
            cleaned_tweet = ' '.join( re.sub(format_regex, " ", tweet.text).split() )
            clean_tweets.append(cleaned_tweet)
        random.shuffle(clean_tweets)
        return clean_tweets

    def clean_tweets_str(self, tweets):
        clean_tweets = []
        format_regex = "(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)"
        for tweet in tweets:
            cleaned_tweet = ' '.join( re.sub(format_regex, " ", tweet).split() )
            clean_tweets.append(cleaned_tweet)
        random.shuffle(clean_tweets)
        return clean_tweets
    
    def create_model(self,states=1):
        raw_text = " ".join(self.tweets)
        return markovify.Text(raw_text,state_size=states)
    
    def create_tweet_long(self):
        return self.model.make_sentence()

    def create_tweet(self):
        return self.model.make_short_sentence(self.tweet_length,tries=1000)
