from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return render(request, 'tweetmood/index.html')


def analysis(request):
    text = request.GET['text']
    return HttpResponse("You submitted:<br>" + text)
