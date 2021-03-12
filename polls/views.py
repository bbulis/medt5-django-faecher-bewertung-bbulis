from django.shortcuts import render
from django.http import HttpResponse

from .models import Subject
# Create your views here.

def index(request):
    subject_list = Subject.objects.all()
    context = {'subject_list': subject_list}
    return render(request, 'polls/index.html', context)

def detail(request, subject_id):
    return HttpResponse('Subject ID %s' % subject_id)

def answers(request, subject_id):
    return HttpResponse('Subject ID %s' % subject_id)

def vote(request, subject_id):
    return HttpResponse('Subject ID %s' % subject_id)