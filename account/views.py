from django.http import HttpResponse

def index(request):
    return HttpResponse(f"{request.user}, it's your account!")
