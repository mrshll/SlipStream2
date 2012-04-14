import show.models
import simplejson, json
from common.util.netflix import flix
from common.util.itunes_scrape import tunes
from common.util.uniq import uniquify
from django.shortcuts import render_to_response, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from show.models import Show, Provider

def login(request):
    c = RequestContext(request)
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html',c)

@login_required
def index(request):
    n             = flix()
    user_profile  = request.user.get_profile()
    providers     = Provider.objects.all()
    total_cost    = 0
    for provider in user_profile.providers.all():
        total_cost = total_cost + provider.cost
    return render_to_response('index.html', {'user'       : request.user,
                                             'userprofile': user_profile,
                                             'cost'       : total_cost  ,
                                             'providers'  : providers
    }, context_instance=RequestContext(request))

@login_required
def auto(request):
    try:
        term = request.GET['term']
        n     = flix()
        i     = tunes()
        u     = uniquify()
        shows = n.autocomplete(term)
        shows = shows + list(i.autocomplete(term))
        shows = u.uni_ord(shows)
        if shows:
            show_json = simplejson.dumps(shows)
            return HttpResponse(show_json)
        return HttpResponse("")
    except Exception as e:
        print(e)

@login_required
def add_show(request):
    try:
        if request.POST and request.POST.get('show'):
            show_name = request.POST.get('show')
            n = flix()
            i = tunes()
            if n.autocomplete(show_name) or i.autocomplete(show_name):
                show     = n.search(show_name)[0]
                show_img = show['box_art']['medium']
                n_id     = show['id']

                new_show, created = Show.objects.get_or_create(name=show_name,
                                                            netflix_id = n_id,
                                                       netflix_img = show_img)
                if created:
                    new_show.status  = "Running"
                    new_show.save()
                request.user.get_profile().shows.add(new_show)
                return HttpResponse('<li><a href="/show/'+str(new_show.id)+'">' + new_show.name + '</a></li>')
        return HttpResponse("FAIL")
    except Exception as e:
        print(e)

@login_required
def remove_show(request):
    try:
        if request.POST and request.POST.get('show'):
            show_name = request.POST.get('show')
            user_profile = user.get_profile()
            s = Show.objects.get(name=show_name)
            user_profile.shows.remove(s)
            return HttpResponse("SUCCESS")
        return HttpResponse("FAIL")
    except Exception as e:
        print(e)

@login_required
def add_provider(request):
    try:
        if request.POST and request.POST.get('provider'):
            provider_name = request.POST.get('provider')
            p = Provider.objects.get(name=provider_name)
            p.save()
            user_profile = request.user.get_profile()
            user_profile.providers.add(p)
            user_profile.save()
            return HttpResponse('<li><a href="/provider/'+str(p.id)+'">' + p.name + '</a></li>')
        return HttpResponse("FAIL")
    except Exception as e:
        print(e)



