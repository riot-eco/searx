# -*- coding: utf-8 -*-

import json
import os
import requests
import urllib.parse
from json import loads

categories = ['general']

def request(query, params):
    '''pre-request callback
    params<dict>:
      method  : POST/GET
      headers : {}
      data    : {} # if method == POST
      url     : ''
      category: 'search category'
      pageno  : 1 # number of the requested page
    '''

    paging = True
    language_support = True
    safesearch = True

    # Add your Bing Search V7 subscription key and endpoint to your environment variables.
    count_wish = 50
    market = params['language'] #"de-DE"
    offset = params['pageno']
    page_no = offset * count_wish
    safesearch = "Moderate"
    subscription_key = os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']
    endpoint = os.environ['BING_API_ENDPOINT'] + "/bing/v7.0/search" + "?count=" + str(
        count_wish) + "&mkt=" + market + "&safesearch=" + safesearch

    params['url'] = endpoint + "q=" + urllib.parse.quote(query)
    params['headers']['Ocp-Apim-Subscription-Key'] = subscription_key

    return params



def response(resp):
    '''post-response callback
    resp: requests response object
    '''
    resp = loads(resp)
    results = []

    for p in resp["webPages"]["value"]:
        res = {'url': p.url, 'title': p.name, 'content': p.snippet}
        results.append(res)

    return results

