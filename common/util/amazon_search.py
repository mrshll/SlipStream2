from amazon.api import AmazonAPI

class amazon_search:
    AMAZON_ACCESS_KEY = 'AKIAIOWIDPGKSCSY72EQ'
    AMAZON_SECRET_KEY = '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'
    AMAZON_ASSOC_TAG  = '7903-2492-0405'

    def new:
        return AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

    def search(query):
        results = a.search(Title=query, SearchIndex='Video')
        return [r.title for r in results]

    def autocomplete(query):
        return search(query)
