from typing import ContextManager
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Subject
from .models import Answer
# Create your views here.

def index(request):
    subject_list = Subject.objects.all()
    for subject in subject_list:
        sub = Subject.objects.get(pk=subject.id)
        subject.answer_count = sub.answer_set.count()
    context = {'subject_list': subject_list}
    return render(request, 'polls/index.html', context)

def detail(request, subject_id):
    # answer_list = Answer.objects.filter(id=subject_id).all()
    # context = {'answer_list': answer_list}
    subject = Subject.objects.get(pk=subject_id)
    # subject.answer_set.create(answer_text="Genau richtig!")
    high = subject.answer_set.filter(answer_text='high').count()
    correct = subject.answer_set.filter(answer_text='correct').count()
    low = subject.answer_set.filter(answer_text='low').count()
    answer = {'subject' : subject, 'high' : high, 'correct' : correct, 'low' : low}
    context = {'answer': answer}
    return render(request, 'polls/detail.html', context)

def answers(request, subject_id):
    return HttpResponse('Subject ID %s' % subject_id)

def vote(request, subject_id):
    return HttpResponse('Subject ID %s' % subject_id)