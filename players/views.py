from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from players.models import Player
from django.template import loader, Context
from forms import PlayerForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def players(request):
    all_players = Player.objects.all().order_by('-last_name')
    t = loader.get_template('players/index.html')
    c = Context({"all_players": all_players})
    return HttpResponse(t.render(c))

def create(request):
    if request.POST:
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/players/')
    else:
        form = PlayerForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('players/create.html', args)

def edit(request, player_id):
    if player_id:
        p = Player.objects.get(id=player_id)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=p)
        if form.is_valid():
        	  form.save()
        	  return HttpResponseRedirect('/players/')
    else:
    	  form = PlayerForm(instance=p)

    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['player'] = p
    return render_to_response('players/edit.html', args)

def delete(request, player_id):
    p = Player.objects.get(id=player_id)
    p.delete()
    return HttpResponseRedirect('/players/')