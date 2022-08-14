import tweepy

"""Twitter API, only used currently for getting API access, reading current trends
and getting tweets with trending hashtags"""
class TwitterApi:

    def __init__(self, api_key, api_key_secret, access_token, access_token_secret) -> None:
        """Gets the API object after authorization
        and authentication.
        Sets coordinates for trend location.
        :param api_key: The consumer API key.
        :param api_key_secret: The consumer API key secret.
        :param access_token: The access token.
        :param access_token_secret: The access token secret.
        """
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(
            access_token,
            access_token_secret
        )
        self.api = tweepy.API(auth)

        # Set Latitude and Longitude, currently these coords are for Los Angeles, CA
        self.lat = 34.0522
        self.lng = -118.2437

    def get_trends(self):
        """Gets the trending search results from Twitter.
        :returns: A dictionary of trending search results.
        """
        closest_loc = self.api.closest_trends(self.lat, self.lng)
        trends = self.api.get_place_trends(closest_loc[0]["woeid"])
        return trends[0]["trends"]


    def extract_hashtags(self, trends):
        """Extracts the hashtags from the trending search results.
        :param trends: A list of trending search results.
        :returns: A lisselft of hashtags.
        """
        hashtags = [trend["name"] for trend in trends if "#" in trend["name"]]
        return hashtags


    def get_n_tweets(self, hashtag, n):
        """Gets the n tweets of the trending hashtag.
        :param hashtag: The trending hashtag.
        :param n: The number of tweets to get.
        :returns: An array of the top n tweets.
        """
        return tweepy.Cursor(
            self.api.search_tweets,
            q = hashtag
        ).items(n) 
    
    def send_selection_query(self,recipient):
        """Sends a message with selection of 5 current trending hashtags
        :param recipient: id of user to send query to
        :returns: true if message is sent, false if error
        """
        trends = self.get_trends()
        tags = self.extract_hashtags(trends)

        new_list = [f'{index + 1}: {elm}' for index, elm in enumerate(tags)]
        message = "Current hashtags:\n" + "\n".join(new_list)
        self.api.send_direct_message(recipient, message)

    # Temp helped function, pull tweets from .txt files to avoid 
    def get_archived_tweets(hashtag):
        with open(f'data/{hashtag}.txt') as f:
            raw_text = f.readlines()
        return raw_text 