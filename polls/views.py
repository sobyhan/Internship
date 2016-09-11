from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.


def index (request):
    req= request
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in lastest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'lastest_question_list': lastest_question_list,
        'req': req,
    }
    return render (request, 'polls/index.html', context)

def details (request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render (request, 'polls/detail.html', {'question': question})

def result (request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render (request, 'polls/results.html', {'question': question})

class IndexView (generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lastest_question_list'

    def queryset (self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView (generic.DetailView):
    model = Question
    template_name = 'polls/details.html'

""" class ResultView (generic.DetailView):
    model = Question
    template_name = 'polls/results.html' """


def vote (request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get (pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render (request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))

