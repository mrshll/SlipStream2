from amazon.api import AmazonAPI

AMAZON_ACCESS_KEY = 'AKIAIOWIDPGKSCSY72EQ'
AMAZON_SECRET_KEY = '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'
AMAZON_ASSOC_TAG  = '7903-2492-0405'

a = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

results = a.search(Title=query, SearchIndex='Video')
for r in results:
    print (r.title)


#def search

#def autocomplete
