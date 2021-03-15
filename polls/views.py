from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Subject
from .models import Answer
# Create your views here.

def index(request):
    subject_list = Subject.objects.all()
    context = {'subject_list': subject_list}
    return render(request, 'polls/index.html', context)

def detail(request, subject_id):
    # answer_list = Answer.objects.filter(id=subject_id).all()
    # context = {'answer_list': answer_list}
    subject = Subject.objects.get(pk=subject_id)
    subject.answer_set.create(answer_text="Genau richtig!")
    return JsonResponse(subject.answer_set.all(), safe=False)

def answers(request, subject_id):
    return HttpResponse('Subject ID %s' % subject_id)

def vote(request, subject_id):
    return HttpResponse('Subject ID %s' % subject_id)