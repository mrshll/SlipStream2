import show.models
import simplejson, json
from netflix import flix
from django.shortcuts import render_to_response


def index(request):
    c = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    else:
        return render_to_response('index.html',c)

@login_required
def user_home(request):
    user_profile = request.user.get_profile()
    return render_to_response('home.html', {'user': request.user,
                                            'userprofile': user_profile,
    }, context_instance=RequestContext(request))

def autocomplete(request):
    n = flix()
    shows = n.doAutocomplete(request['term'])
    json  = simplejson.dumps(shows)
    return HttpResponse(json)
