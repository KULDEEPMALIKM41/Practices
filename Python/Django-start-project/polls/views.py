from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import Http404
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # selected_choice = question.choice_set.filter(pk='2')
        selected_choice = question.choice_set.filter(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes += 1 # Normal method ((work with get function))
        # selected_choice.save()

        # selected_choice.votes = F('votes') + 1 # F Heandle Multipule Request method 1(work with get function)
        # selected_choice.save()

        selected_choice.update(votes=F('votes') + 1) # F Heandle Multipule Request method 2(work with filter function)
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


"""
Test Views:

>>> from django.test import Client
>>> # create an instance of the client for our use
>>> client = Client()
>>> # get a response from '/'
>>> response = client.get('/')
Not Found: /
>>> # we should expect a 404 from that address; if you instead see an
>>> # "Invalid HTTP_HOST header" error and a 400 response, you probably
>>> # omitted the setup_test_environment() call described earlier.
>>> response.status_code
404
>>> # on the other hand we should expect to find something at '/polls/'
>>> # we'll use 'reverse()' rather than a hardcoded URL
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code
200
>>> response.content
b'\n    <ul>\n    \n        <li><a href="/polls/1/">What&#x27;s up?</a></li>\n    \n    </ul>\n\n'
>>> response.context['latest_question_list']
<QuerySet [<Question: What's up?>]>

"""


''' 
--------------"index page"------------------
1. index return http response with strings
from django.http import HttpResponse
def index(request):
	return HttpResponse("Hello, Welcome to first Django Steps")
----------------------------------------------------------------------------
2. index return Question list in last updated
from django.http import HttpResponse
from .models import Question
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(output)
----------------------------------------------------------------------------
3. render template using loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
----------------------------------------------------------------------------
4. render template using shortcut render
from django.shortcuts import render
from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
----------------------------------------------------------------------------
5. generic view index using query_set
from django.views import generic
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
----------------------------------------------------------------------------

--------------"detail.html (with 404 error) page"------------------
1. detail page return http response as strings
from django.http import HttpResponse
def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)
----------------------------------------------------------------------------
2. raising 404 errors with details.html page
from django.http import Http404
from django.shortcuts import render
from .models import Question
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
----------------------------------------------------------------------------
3. raising 404 error with shortcut methods
from django.shortcuts import get_object_or_404, render
from .models import Question
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
----------------------------------------------------------------------------
4. generic view detail
from django.views import generic
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
----------------------------------------------------------------------------
--------------"vote"------------------
1. vote method for choice
from django.http import HttpResponse
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
----------------------------------------------------------------------------
2. vote method render 404 and render to detail.html if successfully get value the render to results
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
----------------------------------------------------------------------------
---------------"result"----------------
1. result method for choice
from django.http import HttpResponse
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
----------------------------------------------------------------------------
2. result method render results.html page
from django.shortcuts import get_object_or_404, render
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
----------------------------------------------------------------------------
3. generic view for result changes in views.py
from django.views import generic
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
----------------------------------------------------------------------------
'''