from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def home(request):
    #string = "Servus!!!"
    return render(request, "projects/index.html")
