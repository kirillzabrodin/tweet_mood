from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .watson import Watson
from .response_formatter import ResponseFormatter
from .holmes import Holmes


def index(request):
    return render(request, 'tweetmood/index.html')


def analysis(request):
    if request.method == 'POST':
        text = request.POST['text']
        watson = Watson()
        response_formatter = ResponseFormatter()
        analysed_text = watson.send_for_analysis(text)
        response_formatter.process(analysed_text)
        response_dict = response_formatter.formatted_response_dict
        holmes = Holmes()
        holmes_analysis = holmes.holmes_analysis(text)
        request.session['text'] = text
        request.session['response_dict'] = response_dict
        request.session['holmes'] = holmes_analysis
        return HttpResponseRedirect("result")
    else:
        return HttpResponse("You did not submit to analysis")


def result(request):
    if 'text' not in request.session:
        return HttpResponse("You did not submit to analysis")
    else:
        response_dict = request.session['response_dict']
        text = request.session["text"]
        holmes = request.session["holmes"]
        return render(request, 'tweetmood/results.html', {'response_dict' : response_dict, "text" : text, "holmes" : holmes})
