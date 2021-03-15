from typing import ContextManager
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Subject
from .models import Answer
# Create your views here.

def index(request):
    """
    function returns subjects and counts all given answers
    """
    subject_list = Subject.objects.all()
    for subject in subject_list:
        sub = Subject.objects.get(pk=subject.id)
        subject.answer_count = sub.answer_set.count()
    context = {'subject_list': subject_list}
    return render(request, 'polls/index.html', context)

def detail(request, subject_id):
    """
    function returns selected subject and all counts diffrent answers
    """
    subject = Subject.objects.get(pk=subject_id)
    high = subject.answer_set.filter(answer_text='high').count()
    correct = subject.answer_set.filter(answer_text='correct').count()
    low = subject.answer_set.filter(answer_text='low').count()
    answer = {'subject' : subject, 'high' : high, 'correct' : correct, 'low' : low}
    context = {'answer': answer}
    return render(request, 'polls/detail.html', context)

def answers(request, subject_id):
    """
    function returns view for one subject with all possible answers
    """
    subject = Subject.objects.get(pk=subject_id)
    context = {'subject': subject}
    return render(request, 'polls/answer.html', context)

def vote(request, subject_id):
    """
    function receives picked answer and added to database
    """
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