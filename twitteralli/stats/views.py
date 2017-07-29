
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
import logging
import logging.config
from stats import twitter_api as tw
from django.http import HttpResponse
import json, urllib


# Create your views here.

def about(request):
    context = {'activePage':'about'}
    return render(request, 'stats/about.html', context)

@login_required
def index(request):    
    context = {'activePage':'index', 'user': request.user}
    user = request.user    
    return render(request, 'stats/index.html', context)

def tweets(request):
    context = {'activePage':'index'}       
    keywords = request.GET.get('keywords')
    max_id = request.GET.get('max_id')
    result_type = request.GET.get('result_type')
    if keywords is not None:
    	api_q = urllib.parse.urlencode({'q':keywords, 'count':15})
    	if max_id is not None:
    		api_q += '&max_id=' + max_id    		
    	print(result_type)	
    	tweets = tw.get_tweets(api_q, result_type)    	       	
    	json_results = [tweet.AsDict() for tweet in tweets]
    	nr_tweets = len(json_results) 
    	print(nr_tweets)
    	print(api_q)   	
    	if (nr_tweets > 0):    		
    		max_id = json_results[nr_tweets-1]['id']    		
    		return HttpResponse(
    			json.dumps({'max_id': max_id, 'tweets':json_results}),
            	content_type="application/json"
            )
    	else:
    		return HttpResponse(
    			json.dumps([]),
            	content_type="application/json"
            )	
    	
    else:
    	return HttpResponse(
            	json.dumps([]),
            	content_type="application/json"
            )	
   	
    

@login_required
def home(request):
    context = {'activePage':'index'}    
    return render(request, 'stats/index.html', context)  

def logout(request):    
    auth_logout(request)    
    return redirect('login')


def login(request):
    context = {'activePage':'login'}
    return render(request, 'stats/login.html', context)        