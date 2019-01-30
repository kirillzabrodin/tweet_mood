from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .watson import Watson
from .tweeterpy import Tweeterpy
import time
from .response_formatter import ResponseFormatter


def index(request):
    return render(request, 'tweetmood/index.html')

def analysis(request):
    if request.method == 'POST':
        text = request.POST['text']
        watson = Watson()
        tweets = Tweeterpy()
        response_formatter = ResponseFormatter()
        text_for_analysis = tweets.get_tweets(text)
        if text_for_analysis == "":
            messages.error(request,'Hmm, nobody is talking about that, ask something else')
            return redirect('/')
        analysed_text = watson.send_for_analysis(text_for_analysis, text)
        print(analysed_text)
        if 'warnings' in analysed_text:
            messages.error(request,"Hmm, Watson didn't like that, try rephrasing the question")
            return redirect('/')
        response_formatter.process(analysed_text)
        response_dict = response_formatter.formatted_response_dict
        request.session['text'] = text
        request.session['response_dict'] = response_dict
        return HttpResponseRedirect("result")
    else:
        return HttpResponse("You did not submit to analysis")


def result(request):
    if 'text' not in request.session:
        return HttpResponse("You did not submit to analysis")
    else:
        response_dict = request.session['response_dict']
        text = request.session["text"]
        return render(request, 'tweetmood/results.html', {'response_dict' : response_dict, "text" : text})
