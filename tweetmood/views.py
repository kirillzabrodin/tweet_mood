from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .watson import Watson
# from .holmes import Holmes
from .tweeterpy import Tweeterpy
import time
from .response_formatter import ResponseFormatter
from django.views.decorators.csrf import csrf_exempt

# holmes = Holmes()

def index(request):
    return render(request, 'tweetmood/index.html')

@csrf_exempt
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
        # holmes_text = holmes.holmes_classify(text)
        if 'warnings' in analysed_text:
            messages.error(request,"Hmm, Watson didn't like that, try rephrasing the question")
            return redirect('/')
        response_formatter.process(analysed_text)
        response_dict = response_formatter.formatted_response_dict
        request.session['text'] = text
        request.session['response_dict'] = response_dict
        return JsonResponse({'response_dict' : response_dict, "text" : text})
    else:
        return HttpResponse("You did not submit to analysis")
