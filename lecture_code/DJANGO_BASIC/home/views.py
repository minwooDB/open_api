from django.shortcuts import render, HttpResponse
import random
import requests
from datetime import datetime


def index(request):
    #return HttpResponse('Welcome to django!')  
    return render(request,'home/index.html') 

def hola(request):
    #return HttpResponse('Hello, my name in minwoo')
    return render(request,'home/hola.html')

def dinner(request):
    menus = ['피자', '치킨','족발','라면']
    dinner = random.choice(menus)
    #return HttpResponse(f'오늘의 저녁메뉴는 {dinner}입니다.')
    return render(request,'home/dinner.html',{'menus':menus,'dinner':dinner})

def lotto(request):
    number = range(1,46)
    my_lotto = sorted(random.sample(number,6))
    return HttpResponse(f'오늘의 추천번호는{my_lotto}입니다.')

def lotto2(request):
    URL_GetLottoNum = "https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=882"
    resp = requests.get(URL_GetLottoNum)
    jsResult = resp.json()
    print(jsResult)
    lotto_nums = []
    for i in range(1,7):
        lotto_nums.append(jsResult[f'drwtNo{i}'])
    print(lotto_nums)
    number = range(1,46)
    my_lotto = sorted(random.sample(number,6))
    match = set(my_lotto) & set(lotto_nums)
    rank = len(match)
    cnt = 1

    while rank <5:
        cnt += 1
        my_lotto = random.sample(range(1,46),6)
        match = set(my_lotto) & set(lotto_nums)
        rank = len(match)
    return render(request,'home/lotto2.html',{'lotto_nums':lotto_nums,'my_lotto':my_lotto,'cnt':cnt})

def hello(request, name):
    return render(request, 'home/hello.html', {'name':name})

def introduce(request, name, age):
    return render(request, 'home/introduce.html', {'name':name,'age':age})

def square(request, width, height):
    result = width*height
    return render(request, 'home/area.html', {'width':width,'height':height, 'result':result})

def template_language(request):
    menus = ['아메리카노','카페라떼','마끼야또','루이보스','프라푸치노']
    cafes = ['starbucks','coffeebean','hollys','ediya']
    my_sentence = 'Life is short, you need Python'
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus':menus,
        'cafes':cafes,
        'my_sentence':my_sentence,
        'datetimenow':datetimenow,
        'empty_list':empty_list,

    }
    return render(request, 'home/template_language.html', context)

def image(request):
    return render(request, 'home/template_language.html', context)

def isbirth(request):
    today = datetime.now()
    if today.month == 6 and today.day == 27:
        result = True
    else:
        result = False
    return render(request, 'home/isbrith.html',{'result':result})

#글자의 순서를 뒤집어도 원래의 글자가 입력되는 
#회문이라고 표시하고 , 아니면 아니라고 표시하는 페이지
def ispal(request, word):
    if word == word[::-1]:
        result = True
    else:
        result = False
    return render(request, 'home/ispal.html', {'word':word,'result' :result})


#GET / POST

def throw(request):
    return render(request, 'home/throw.html')

def  catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    return render(request, 'home/catch.html', {'message':message, 'message2':message2})

def input_word(request):
    return render(request, 'home/input_word.html')

def  ispal2(request):
    word = request.GET.get('input_word')
    if word == word[::-1]:
        result = True
    else:
        result = False
    return render(request, 'home/ispal2.html', {'word':word,'result' :result})

def user_new(request):
    return render(request, 'home/user_new.html')
def user_create(request):
    user_name = request.POST.get('name')
    user_password = request.POST.get('pwd')

    return render(request, 'home/user_create.html',{'user_name':user_name,'user_password':user_password})

def static_example(request):
    return render(request, 'home/static_example.html')
