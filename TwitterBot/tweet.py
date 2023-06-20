import tweepy

api_key = 'fauNfnpN4AhT1ZIZtxLhFV4hj'
api_secret_key = 'nZHZRwcfbRsH4w50Vod4jOMyATqLSn2PkUrVUXPYZuIe4aP6pd'
bearer_token = r'AAAAAAAAAAAAAAAAAAAAAI83oQEAAAAAceOmqD0dbxmsHa6ogYghuXHOpZg%3Dx71Mo58isZbO2sYlPAuyxfccB6B98gSkcUDC2h4uEidy3ocbcH'
access_token = '1657817293177630721-F92K7t87GMKfio784keLTFqDGCmTmu'
acess_token_secret = 'i3W68MS9bBzFgjB0LjUEQgjW4InidvqeE4yTTKehNuDMq'

# client = tweepy.Client(bearer_token, api_key, api_secret_key, access_token, acess_token_secret)

# auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, acess_token_secret)


# api = tweepy.API(auth)

# # client.create_tweet(text="Hello  World please smile ")
# user = api.verify_credentials()
# print(user.followers_count)

# generous bot
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

# for follow in tweepy.Cursor(api.followers,screen_name).items():
#     if not follow.following:
#         follow.follow()
#         print(f"Followed {follow.name}")

# search_string = 'python'
# numberOfTweets = 2

# for tweet in tweepy.Cursor(api.search_tweets, search_string).items(numberOfTweets):
#     try:
#         tweet.favorite()
#         print("I liked that tweet")
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break

def get_tweets(username):
         
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
 
        # Access to user's access key and access secret
        auth.set_access_token(access_token, acess_token_secret)
 
        # Calling api
        api = tweepy.API(auth)
 
        # 200 tweets to be extracted
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)
 
        # Empty Array
        tmp=[]
 
        # create array of tweet information: username,
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
        for j in tweets_for_csv:
 
            # Appending tweets to the empty array tmp
            tmp.append(j)
 
        # Printing the tweets
        print(tmp)
 
 
# Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("twitter-handle")
