from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from players.models import Player
from django.template import loader, Context
from forms import PlayerForm
from django.core.context_processors import csrf

def index(request):
    all_players = Player.objects.all().order_by('-last_name')
    template = loader.get_template('players/index.html')
    context = Context({"all_players": all_players})
    return HttpResponse(template.render(context))

def players(request):
    all_players = Player.objects.all().order_by('-last_name')
    template = loader.get_template('players/players.html')
    context = Context({"all_players": all_players})
    return HttpResponse(template.render(context))

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
        player = Player.objects.get(id=player_id)
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
        	  form.save()
        	  return HttpResponseRedirect('/players/')
    else:
    	  form = PlayerForm(instance=player)

    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['player'] = player
    return render_to_response('players/edit.html', args)

def delete(request, player_id):
    player = Player.objects.get(id=player_id)
    player.delete()
    return HttpResponseRedirect('/players/')