from django.shortcuts import render
def greeting(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

# Create your views here.
