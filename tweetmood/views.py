from django.shortcuts import render
from django.http import JsonResponse
from .watson import Watson
from .holmes import Holmes
from .tweeterpy import Tweeterpy
from .response_formatter import ResponseFormatter
from django.views.decorators.csrf import csrf_exempt

holmes = Holmes()

def index(request):
    return render(request, 'tweetmood/index.html')

@csrf_exempt
def analysis(request):
    text = request.POST['text']
    watson = Watson()
    tweets = Tweeterpy()
    response_formatter = ResponseFormatter()
    text_for_analysis = tweets.get_tweets(text)
    if text_for_analysis == '':
        return JsonResponse({'response' : 'Hmm, nobody is talking about that, ask something else'})
    holmes_result = holmes.holmes_classify(text)
    watson_result = watson.send_for_analysis(text_for_analysis, text)
    if 'warnings' in watson_result:
        return JsonResponse({'response' : "Hmm, Watson didn't like that, try rephrasing the question"})
    response_formatter.process(watson_result)
    watson_result = response_formatter.formatted_response_dict
    return JsonResponse({'watson_result' : watson_result, "response" : text, "holmes_result" : holmes_result})
