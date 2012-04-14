import itunes

class tunes():
    def autocomplete(self,arg):
        try:
            shows = itunes.search(query=arg, media="tvShow")[:5]
            return [x.name for x in shows]
        except Exception as e:
            print (e)
    def search(self,arg):
        return itunes.search(query=arg, media="tvShow")
    def getTitleInfo(self,itunes_id):
        return itunes.lookup(itunes_id)

