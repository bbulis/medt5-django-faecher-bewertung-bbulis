from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def detail(request, subject_id):
    return HttpResponse({'subject_id': subject_id, 'anwser_count': 0})

def answer(request, subject_id):
    return HttpResponse({'subject_id': subject_id, 'answers': {'answer': '1', 'answer': '2'}})

def vote(request, subject_id, answer_text):
    return HttpResponse({'subject_id': subject_id, 'answer': answer_text})