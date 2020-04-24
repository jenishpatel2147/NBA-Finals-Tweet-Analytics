import tweepy

# Fill the X's with the credentials obtained by
# following the above mentioned procedure.
consumer_key = "2i0a8rYG1b5pGWDEbXKgh8gsF"
consumer_secret = "zW3qC30mYq2F8etChXQYU4Kr5bdus7ftsAgCBQ3jHQnYpZUp14"
access_key = "3936941474-q2frOK04onmcTxry1UuL8sZPB3LSBKwisqxrpxE"
access_secret = "PqllJJFSuNkzJpVSgPfa2jopRDXYbPeSkRVrn2g4KTTeh"

# Function to extract tweets
def get_tweets(username):

        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)

        # Calling api
        api = tweepy.API(auth)

        # 200 tweets to be extracted
        number_of_tweets= 1
        tweets = api.user_timeline(screen_name=username)

        # Empty Array
        tweetstore=[]

        # create array of tweet information: username,
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
        for x in tweets_for_csv:

            # Appending tweets to the empty array tmp
            tweetstore.append(x)

        # Printing the tweets
        print(tweetstore)


# Driver code
if __name__ == '__main__':

    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("@realDonaldTrump")
