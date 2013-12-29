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
search_offsets  = [0]
sort_mode       = 2

# initialize an api object
yelp_api = YelpAPI(consumer_key, consumer_secret, token, token_secret)

# look here for the terms you can use for searching and their meaning
# http://www.yelp.com/developers/documentation/v2/search_api#searchMSL
for offset in search_offsets:
    print "At offset: %d" % offset
    search_results = yelp_api.search_query(
                         location = search_location,
                         term     = search_term,
                         offset   = offset,
                         sort     = sort_mode
                     )

    for biz in search_results.get('businesses'):
        #pprint(b)
        print '%s - %s - %s - %s' % ( biz.get('name'), biz.get('rating'), biz.get('location').get('address'), biz.get('location').get('postal_code') )