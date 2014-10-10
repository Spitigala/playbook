from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from players.models import Player
from django.template import loader, Context
from forms import PlayerForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
# from someapp.forms import StudentForm

def players(request):
    all_players = Player.objects.all().order_by('-last_name')
    # context = {"all_players": all_players}
    # return render(request, 'players/index.html', context)
    t = loader.get_template('players/index.html')
    c = Context({"all_players": all_players})
    return HttpResponse(t.render(c))

# def players_template(request):
#     all_players = Player.objects.all().order_by('-last_name')
#     context = {"all_players": all_players}
#     return render(request, 'players/index.html', context)

# class PlayerTemplate(TemplateView):
#     template_name = 'player_class.html'

#     def get_context_data(self, **kwargs):
#         context = super(PlayerTemplate, self).get_context_data(**kwargs)
#         all_players = Player.objects.all().order_by('-last_name')
#         context = {"all_players": all_players}
#         return context

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