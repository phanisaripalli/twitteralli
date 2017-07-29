import twitter

config = {}
exec(open("config.py").read(), config)


api = twitter.Api(consumer_key=config["consumer_key"],
                  consumer_secret=config["consumer_secret"],
                  access_token_key=config["access_key"],
                  access_token_secret=config["access_secret"]
                 )

def get_tweets() {
	results = api.GetSearch(raw_query="q=saripalli&result_type=recent&count=10")
	#print (results)
	return results
}