from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
    analysed_text = watson.send_for_analysis(text_for_analysis, text)
    if 'warnings' in analysed_text:
        return JsonResponse({'response' : "Hmm, Watson didn't like that, try rephrasing the question"})
    response_formatter.process(analysed_text)
    response_dict = response_formatter.formatted_response_dict
    return JsonResponse({'response_dict' : response_dict, "response" : text, "holmes_result" : holmes_result})
