from django.shortcuts import render
from decouple import config
import requests

def index(request):
    return render(request, 'utilities/index.html')

def papago(request):
    return render(request, 'utilities/papago.html')

def translated(request):
    korean = request.GET.get('text')

    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')

    papago_url = "https://openapi.naver.com/v1/papago/n2mt"

    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret,
    }
    data = {
        'source': 'ko',
        'target': 'en',
        'text': korean,
    }
    papago_response = requests.post(papago_url, data=data, headers=headers).json()
    english = papago_response['message']['result']['translatedText']

    context = {'korean':korean, 'english':english}
    return render(request, 'utilities/translated.html', context)