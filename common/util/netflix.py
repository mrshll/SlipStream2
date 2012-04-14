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
        autocomplete = self.netflixClient.catalog.searchStringTitles(arg)
        shows = []
        for item in autocomplete:
            shows.append(item['title']['short'])
        return shows

    def getTitleInfo(self, movie):
        # grab the format for this movie
        disc = \
            self.netflixClientDisc(movie['catalog_title'],self.netflixClient)
        formats = disc.getInfo('formats')
        synopsis = disc.getInfo('synopsis')
        cast = disc.getInfo('cast')
        return {"disk":disc, "formats":formats, "synopsis":synopsis,
                "cast":cast}


