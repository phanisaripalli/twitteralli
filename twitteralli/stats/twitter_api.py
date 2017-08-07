import twitter
import os

config = {}
exec(open(os.path.dirname(os.path.realpath(__file__)) + "/config.py").read(), config)


api = twitter.Api(consumer_key=config["consumer_key"],
                  consumer_secret=config["consumer_secret"],
                  access_token_key=config["access_key"],
                  access_token_secret=config["access_secret"]
                 )

def get_tweets(api_k, result_type="recent"):
	additional_param = "&result_type="+result_type
	results = api.GetSearch(raw_query=api_k+additional_param)
	return results

def get_trends():
    trends = api.GetTrendsCurrent()
    return trends   
