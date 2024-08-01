from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    # return HttpResponse("Hello World")
    return render(request, 'main.html')

def main2(request):
    # return HttpResponse("오늘 점심 밖에 안 나갈란다")
    return render(request, 'main2.html')

def hjt(request):
    return render(request, 'hjt.html')