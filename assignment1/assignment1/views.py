from django.http import HttpResponse

def assignment1(request):
    return HttpResponse("<h1><b>Hello, Django!</b.</h1>")