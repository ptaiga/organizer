from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'account/index.html')
    # return HttpResponse(f"{request.user}, it's your account!")
