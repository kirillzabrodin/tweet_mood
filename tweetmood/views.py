from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .watson import Watson
from .response_formatter import ResponseFormatter

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
        request.session['text'] = text
        request.session['response_dict'] = response_dict
        return JsonResponse(request)
    else:
        return HttpResponse("You did not submit to analysis")


def result(request):
    if 'text' not in request.session:
        return HttpResponse("You did not submit to analysis")
    else:
        response_dict = request.session['response_dict']
        text = request.session["text"]
        return render(request, 'tweetmood/results.html', {'response_dict' : response_dict, "text" : text})
