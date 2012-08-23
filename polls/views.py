# Create your views here.
from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from polls.models import Poll, Choice
from django.core.urlresolvers import reverse
#from django.template import loader, Context


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')
# Technique 1
#    t=loader.get_template('polls/index.html')
#    c = Context({
#                 'latest_poll_list':latest_poll_list
#        })
#    return HttpResponse(t.render(c))
    
#Technique 2 
#    return render_to_response('polls/index.html', {
#                'latest_poll_list':latest_poll_list
#            })

#Technique 3 : Passes the user to the template(index.html)    
    return render(request, 'polls/index.html', {
                'latest_poll_list':latest_poll_list
            })

def detail(request, poll_id):
    #return HttpResponse('You are looking at poll %s' % poll_id)
#    try:
#        p = Poll.objects.get(pk=poll_id)
#    except Poll.DoesNotExist:
#        raise Http404
    p = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html',{'poll':p})

def results(request, poll_id):
    #return HttpResponse('You are looking at the results of poll %s' % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html',{'poll':p})


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
