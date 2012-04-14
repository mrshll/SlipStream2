from Netflix import *
import getopt
import time

class flix():
    APP_NAME   = 'SlipStream'
    API_KEY    = 'gttph83vhtfvjxfsskqx5mr7'
    API_SECRET = 'jPgUAyfAQ2'
    CALLBACK   = ''
    netflixClient = NetflixClient(APP_NAME, API_KEY, API_SECRET, CALLBACK,
                                      True)

    # takes a string arg and returns full data for the search in a nested list
    # in [title][regular] format: print info['title']['regular']
    def search(self, arg):
        data = self.netflixClient.catalog.searchTitles(arg,0,10)
        return data

    # takes a string arg and returns a nested list with [title, short]
    def autocomplete(self, arg):
        try:
            autocomplete = self.netflixClient.catalog.searchStringTitles(arg)
            shows = []
            for item in autocomplete:
                shows.append(item['title']['short'])
            return shows
        except Exception as e:
            print(e)

    def getTitleInfo(self, movie):
        # grab the format for this movie
        disc = NetflixDisc(['catalog_title'], self.netflixClient)
        formats = disc.getInfo('formats')
        synopsis = disc.getInfo('synopsis')
        cast = disc.getInfo('cast')
        return {"disk":disc, "formats":formats, "synopsis":synopsis,
                "cast":cast}

    def getEpisodeList(self, name):
        data = self.netflixClient.catalog.searchStringTitles('Mad Men')
        print(data)
