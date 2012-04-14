import show.models
import simplejson, json
from common.util.netflix import flix
from django.shortcuts import render_to_response, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

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
    if request.POST and request.POST.get('show_name'):
        show_name = request.POST.get('show_name')
        n = flix()
        if n.autocomplete(show_name):
            new_show, created = Show.objects.get_or_create(name=show_name)
            if created:
                new_show.status  = "Running"
                new_show.save()
            request.user.get_profile().shows.add(new_show)
            return HttpResponse('<li><a href="/show/'+str(new_show.id)+'">' + new_show.name + '</a></li>')
    return HttpResponse("")
