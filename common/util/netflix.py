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
            autocomplete = \
                self.netflixClient.catalog.searchStringTitles(str(arg))
            shows = []
            if len(autocomplete) == 1:
                return [autocomplete]
            else:
                for item in autocomplete:
                    shows.append(item['title']['short'])
                return shows
        except Exception as e:
            print(e)

    def getTitleInfo(self, movie):
        # grab the format for this movie
        disc = NetflixDisc(movie['catalog_title'], self.netflixClient)
        formats = disc.getInfo('formats')
        synopsis = disc.getInfo('synopsis')
        cast = disc.getInfo('cast')
        return {"disk":disc, "formats":formats, "synopsis":synopsis,
                "cast":cast}

    def getEpisodes(self, show_id):
        raw_episodes = self.netflixClient.catalog.getTitle(show_id)
        episodes = []
        for raw_episode in raw_episodes:
            episodes.append({name:raw_episode['title']['episode_short']})
        return episodes

    def provide(self, show_name):
        if len(self.search(show_name)) >= 1:
            return True
        return False
