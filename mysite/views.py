from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("<h1><strong>Roshan</strong></h1>")
    # params = {'name':'roshan','place':'India'}
    # return render(request,'index.html',params)
    return render(request,'index.html')
# def resume(request):
#     return HttpResponse("<p>My name is Roshan Kumar </p>")
# def bio(request):
#     return HttpResponse("<p>Hello, I am Roshan , I live in Patna <a href = '/'>Home</a></p>")

def removepunc(request):
    #Get the text
    # djText= request.GET.get('text','default')
    # fullcaps = request.GET.get('fullcaps','off')
    # characterCnt =request.GET.get('charactercount','off')
    # lowered = request.GET.get('lowercase','off')
    djText = request.POST.get('text', 'default')
    fullcaps = request.POST.get('fullcaps', 'off')
    characterCnt = request.POST.get('charactercount', 'off')
    lowered = request.POST.get('lowercase', 'off')

    print(fullcaps)
    print(djText.upper())
    if fullcaps == "on":
        CaptalizeText = djText.upper()
        # return HttpResponse("<p> RemovePunc <a href='/'>Home</a></p>")
        params = {'purpose':'Text Analyzation','CaptalizeText':CaptalizeText}
        return render(request,'capatalize.html',params)
    elif characterCnt == "on":
        sentence = list(djText)
        Count = len(sentence)
        params = {'CharacterCount': Count}
        return render(request,'count.html',params)
        # return HttpResponse("No. of Character in sentence = " +str(Count))
    elif lowered == "on":
        LoweredText = djText.lower()
        params = {'purpose':'to lower the letters','LowerText': LoweredText}
        return render(request,'lowerized.html',params)
    else:
        return HttpResponse("<h5>Error 404</h5>")
