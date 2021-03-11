from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def detail(request, subject_id):
    return HttpResponse('Subject ID %s' % subject_id)

def answers(request, subject_id):
    return HttpResponse('Subject ID %s' % subject_id)

def vote(request, subject_id):
    return HttpResponse('Subject ID %s' % subject_id)