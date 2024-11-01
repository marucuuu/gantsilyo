from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def product(request):
    return render(request, 'home/product.html')

def about(request):
    return render(request, 'home/about.html')