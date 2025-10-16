from django.shortcuts import render
from django.shortcuts import redirect

def redirect_to_gallery(request):
    return redirect('/gallary')
def home(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')

# Create your views here.
