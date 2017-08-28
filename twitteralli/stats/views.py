
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
import logging
import logging.config
from stats import twitter_api as tw
from django.http import HttpResponse
import json, urllib
import stats.twitter_stats as ts


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
        tweets = tw.get_tweets(api_q, result_type)
        json_results = [tweet.AsDict() for tweet in tweets]
        nr_tweets = len(json_results)
        print(json_results[0])
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

def trends(request):    
    trends = tw.get_trends()    
    
    json_results = [trend.AsDict() for trend in trends]
    results = []  
    for result in json_results:
        if ('tweet_volume' in result):
            url = '<a href="'+ result['url'] +'">'+ 'Fooo' +'</a>'
            results.append({'name' : result['name'], 'volume' : result['tweet_volume'], 'url':url})                                 

    return HttpResponse(
            json.dumps({'trends': results[0:10]}),
            content_type="application/json"
    )   

def stream_overview(request):

    overview = ts.get_overview()
    results = []
    results.append({'search_key': overview[0], 'total_tweets': overview[1], 'distinct_users':overview[2], 'since':overview[3]})

    return HttpResponse(
        json.dumps({'stream_stats': results}),
        content_type="application/json"
    )

def stream_popular_hashtags(request):

    popular_hashtags = ts.poular_hashtags()
    results = []
    for hashtag in popular_hashtags:
        results.append({'hashtag': hashtag[0], 'total_tweets': hashtag[1]})

    return HttpResponse(
        json.dumps({'stream_stats': results}),
        content_type="application/json"
    )

def stream_minutely_distribution(request):

    distributions = ts.minutly_dsitribution()
    results = []
    for distribution in distributions:
        results.append({'hr-min': distribution[0], 'total_tweets': distribution[1]})

    return HttpResponse(
        json.dumps({'stream_stats': results}),
        content_type="application/json"
    )

def stream_avg_distribution(request):

    overview = ts.avg_distribution()
    results = []
    results.append({'avg': overview[0]})

    return HttpResponse(
        json.dumps({'stream_stats': results}),
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

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response    

def foo(request):
    context = {'activePage':'index'}    
    return render(request, '404.html', context)     