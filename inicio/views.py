from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myHomeView(request,*args, **kwargs):
	print(args,kwargs)
	print(request.user)
	myContext = {
	 	"myText": "Esto es sobre nosotros",
        "myNumber": 123,
        "myList":[33,44,55],
    }
	return render(request,"home.html",myContext)

def anotherView(request):
	return render(request,"home2.html",{})

def otraView(request, *args, **kwargs):
	myContext = {
	 	"myList": [12, 28, 78, 6,"cadena",False],
        "Texto": "Textito",
        "unnumero": 152,
        "booleano": False
    }
	return render(request,"utilizabase.html",myContext)

def vistaCreada(request):
	return HttpResponse('<h1>Creando nuevas vistas !!!!</h1> <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nec nibh laoreet ex egestas ornare sit amet a dolor. Integer viverra rhoncus tristique. Aenean ac urna sed felis porttitor fermentum sit amet sed mi. Nam luctus augue quis consectetur ultricies. Ut quis hendrerit nulla. Duis maximus dignissim turpis, sit amet efficitur lorem. Nulla faucibus eget tortor eu finibus. Suspendisse pellentesque est a nunc aliquet, dapibus ultricies nisi vehicula. Donec a erat odio. Donec rhoncus pellentesque ante, in maximus lectus sagittis sed. Phasellus in ex leo.</p>')
