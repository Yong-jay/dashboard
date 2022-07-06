from django.http import HttpResponse
from django.shortcuts import render

def index(req):
    context = {

    }
    # 처리 요청이 들어오면 index.html 페이지로 처리하겠다.
    # index.html 페이지를 그릴 때 어떤 context(데이터)를 전달할지에 대한 요소
    return render(req, "index.html", context=context)