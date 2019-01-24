from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .watson import ToneAnalyzer
from .watson_formatter import WatsonFormatter

def index(request):
    return render(request, 'tweetmood/index.html')

def analysis(request):
    text = request.GET['text']
    tone_analyzer = ToneAnalyzer()
    watson_formatter = WatsonFormatter()
    analysed_text = tone_analyzer.send_for_analysis(text)
    text = watson_formatter.formatter(analysed_text)
    return HttpResponse("You submitted:<br>" + text + "<br>" + "Your results show that this text contains:<br>" + "Value : %s" % text)
