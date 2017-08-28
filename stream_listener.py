import tweepy


consumer_key = "VJ04UUrmTfHvrebpTuZ67wwBH"
consumer_secret = "fVtCMSYJM3RTzvymMS2F2n39ee2sgufru6KfwPwEXOJnTFso9R"
access_key = "58382701-2qPEY5GRmNErJDcUkI6fwBxQVklx7GdeYzOjUNL2X"
access_secret = "Rg2OhzABmI9gtZGYEh4UqrwX7nGVjZf10sgQn2Riqj2b2"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):


    def get_stream(self):
        if stream is None:
            myStreamListener = MyStreamListener()
            stream = tweepy.Stream(auth=auth, listener=myStreamListener)

        return stream

    def on_status(self, status):
        print(status.text)


stream_listener = MyStreamListener()
stream = tweepy.Stream(auth=auth, listener=stream_listener)
stream.filter(track=['trump'])