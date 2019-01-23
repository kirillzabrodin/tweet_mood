from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .watson import ToneAnalyzer

def index(request):
    return render(request, 'tweetmood/index.html')

def analysis(request):
    text = request.GET['text']
    tone_analyzer = ToneAnalyzer()
    analysed_text = tone_analyzer.send_for_analysis(text)
    return HttpResponse("You submitted:<br>" + text + "<br>" + "Your results:<br>" + analysed_text)
