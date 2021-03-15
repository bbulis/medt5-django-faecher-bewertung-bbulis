from typing import ContextManager
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
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
    subject = Subject.objects.get(pk=subject_id)
    context = {'subject': subject}
    return render(request, 'polls/answer.html', context)

def vote(request, subject_id):
    subject = Subject.objects.get(pk=subject_id)
    try:
        selected = request.POST.get('answer')
        subject.answer_set.create(answer_text = selected)
        subject.save()
    except:
        return render(request, 'polls/detail.html', {
            'error_message': 'Kein Fach ausgewählt'
        })
    else:
        return redirect('index')