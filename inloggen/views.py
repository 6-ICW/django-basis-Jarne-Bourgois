from django.shortcuts import render

# Create your views here.



def htmlResponse(request):

    req = request.GET
    return render(request,"start.html")