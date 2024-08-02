from django.shortcuts import render
from burgers.models import Burger


def main(request):
    # return HttpResponse("Hello World")
    return render(request, 'main.html')

def main2(request):
    # return HttpResponse("오늘 점심 밖에 안 나갈란다")
    return render(request, 'main2.html')

def hjt(request):
    return render(request, 'hjt.html')

def burger_list(request):
    burgers = Burger.objects.all()
    print(f"전체 햄버거 목록 : {burgers}")
    context = {'burgers': burgers}
    return render( request, 'burger_list.html', context)