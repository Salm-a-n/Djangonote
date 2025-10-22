from django.shortcuts import render
from .forms import RegForm
from .models import Customer
def movies(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            cust = Customer()
            cust.movie = form.cleaned_data['movie']
            cust.year = form.cleaned_data['year']
            cust.save()
            return render(request,'success.html',{
                 'movie': cust.movie,
                 'year':cust.year
            })
    else:
        form = RegForm()
    return render(request,'index.html',{'form':form})