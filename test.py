from pprint import pprint

# Documentation: http://github.com/gfairchild/yelpapi
from yelpapi import YelpAPI

consumer_key    = 'MrJMq067KxJXDJ4htdUQvA'
consumer_secret = '49qkGA2-97FMpYwM7ucsjAnLehE'
token           = '_IB2O4d99UyNzIgWMJPG7UMSCRtLLWy1'
token_secret    = 'wZPFX56O173NJNTsZ12GS91W3OQ'

# search arguments
search_location = 'san diego'
search_term     = 'mexican restaurant'

# initialize an api object
yelp_api = YelpAPI(consumer_key, consumer_secret, token, token_secret)

# look here for the terms you can use for searching and their meaning
# http://www.yelp.com/developers/documentation/v2/search_api#searchMSL
search_results = yelp_api.search_query(
                     location = search_location,
                     term     = search_term,
                 )
for b in search_results.get('businesses'):
    pprint(b)
