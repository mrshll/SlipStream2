import show.models
import simplejson, json
from common.util.netflix import flix
from django.shortcuts import render_to_response, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from show.models import Show

def login(request):
    c = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html',c)

@login_required
def index(request):
    user_profile = request.user.get_profile()
    return render_to_response('index.html', {'user': request.user,
                                             'userprofile': user_profile,
    }, context_instance=RequestContext(request))

@login_required
def auto(request):
    try:
        n     = flix()
        shows = n.autocomplete(request.GET['term'])
        if shows:
            show_json = simplejson.dumps(shows)
            return HttpResponse(show_json)
        return HttpResponse("")
    except Exception as e:
        print(e)

@login_required
def add(request):
    try:
        if request.POST and request.POST.get('show'):
            show_name = request.POST.get('show')
            n = flix()
            if n.autocomplete(show_name):
                show     = n.search(show_name)[0]
                show_img = show['box_art']['medium']
                print(show['box_art'])
                n_id  = show['id']

                new_show, created = Show.objects.get_or_create(name=show_name,
                                                            netflix_id = n_id,
                                                       netflix_img = show_img)
                if created:
                    new_show.status  = "Running"
                    new_show.save()
                request.user.get_profile().shows.add(new_show)
                return HttpResponse('<li><a href="/show/'+str(new_show.id)+'">' + new_show.name + '</a></li>')
        return HttpResponse("didn't add show", status=403)
    except Exception as e:
        print("Error Adding: " + e)
