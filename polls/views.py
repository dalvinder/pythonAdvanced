# Create your views here.
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from polls.models import Poll, Choice
from django.core.urlresolvers import reverse
#from django.template import loader, Context

def vote(request, poll_id):
    #return HttpResponse('You are voting for poll %s' % poll_id)
    p = get_object_or_404(Poll,pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
                'poll':p,
                'error_message':'You did not select a choice',
            })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results',args=(p.id,)))    
