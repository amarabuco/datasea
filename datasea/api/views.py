from django.shortcuts import render, HttpResponse
from django.http import FileResponse, StreamingHttpResponse, JsonResponse

import os

# Create your views here.


def html(request, nome):
    #context = {}
    # return render(request, 'app/index.html', context)
    caminho = os.path.abspath('./data/' + nome+'.html')
    content = open(caminho, "r", encoding="utf-8")
    return HttpResponse(content)


def csv(request, nome):
    #context = {}
    # return render(request, 'app/index.html', context)
    caminho = os.path.abspath('./data/' + nome+'.csv')
    return FileResponse(open(caminho, 'rb'), )


def json(request, nome):
    #context = {}
    # return render(request, 'app/index.html', context)
    caminho = os.path.abspath('./data/' + nome+'.json')
    content = open(caminho, "r")
    return HttpResponse(content)
