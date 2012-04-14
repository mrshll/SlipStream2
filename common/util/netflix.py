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

    def doSearch(self, discs, arg):
        ######################################
        # Search for titles matching a string.
        # To view all of the returned object,
        # you can add a simplejson.dumps(info)
        ######################################
        print "*** RETRIEVING MOVIES MATCHING %s ***" % arg
        data = self.netflixClient.catalog.searchTitles(arg,0,10)
        for info in data:
            print info['title']['regular']
            discs.append(info)

    # takes a string arg and returns a nested list with [title, short]
    def doAutocomplete(self, arg):
        autocomplete = self.netflixClient.catalog.searchStringTitles(arg)
        return autocomplete

    def getTitleInfo(self, movie):
        # grab the format for this movie
        disc =
            self.netflixClientDisc(movie['catalog_title'],self.netflixClient)
        formats = disc.getInfo('formats')
        synopsis = disc.getInfo('synopsis')
        cast = disc.getInfo('cast')
        return {"disk":disc, "formats":formats, "synopsis":synopsis,
                "cast":cast}


