from django.shortcuts import render
from .forms import RegForm,ContactForm
from .models import Customer,Contact
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
def contact(request):
    if request.method== 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            con=Contact()
            con.full_name=form.cleaned_data['full_name']
            con.email=form.cleaned_data['email']
            con.phone=form.cleaned_data['phone']
            con.save()
            return render(request,'contactsave.html',{
                'name':con.full_name
            })
    else:
        form=ContactForm()
    return render(request,'contact_from.html',{'form':form})