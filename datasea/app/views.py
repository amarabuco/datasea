from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {}
    return render(request, 'app/index.html', context)


def now(request):
    context = {}
    return render(request, 'app/now.html', context)


def api(request):
    context = {}
    return render(request, 'app/api.html', context)


def market(request):
    context = {}
    return render(request, 'app/market.html', context)
