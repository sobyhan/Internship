from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index (request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in lastest_question_list])
    return HttpResponse(output)

def details (request, question_id):
    return HttpResponse ("Now You're looking to question No. %s." % question_id)

def result (request, question_id):
    response = "You're looing at the result of question %s."
    return HttpResponse (response % question_id)

def vote (request, question_id):
    return HttpResponse ("You're voting of question %s." % question_id)



