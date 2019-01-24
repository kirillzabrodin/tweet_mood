from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .watson import ToneAnalyzer


def index(request):
    return render(request, 'tweetmood/index.html')


def analysis(request):
    if request.method == 'POST':
        text = request.POST['text']
        watson = Watson()
        watson = watson.send_for_analysis(text)
        request.session['text'] = text
        request.session['analysed_text'] = analysed_text
        return HttpResponseRedirect("result")
    else:
        return HttpResponse("You did not submit to analysis")


def result(request):
    if 'text' not in request.session:
        return HttpResponse("You did not submit to analysis")
    else:
        session = [request.session['text'], request.session['analysed_text']]
        return HttpResponse("You submitted:<br>" + session[0] + "<br>" + "Your results:<br>" + session[1])
