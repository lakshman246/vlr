from django.http import HttpResponse
from django.shortcuts import render
#def index(request):
    #return HttpResponse("Rango says hey there partner!")
    #return HttpResponse("Hello <br><a href='/rango/about/'>About</a>")
def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page :<a href='/rango/'>Back</a>")
