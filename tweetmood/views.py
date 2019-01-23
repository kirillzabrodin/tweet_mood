from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .watson import Watson

def index(request):
    return render(request, 'tweetmood/index.html')

def analysis(request):
    text = request.GET['text']
    watson = Watson()
    analysed_text = watson.send_for_analysis(text)
    return HttpResponse("You submitted:<br>" + text + "<br>" + "Your results:<br>" + analysed_text)
