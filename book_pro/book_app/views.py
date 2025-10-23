from django.shortcuts import render
from .forms import BookForm
from .models import Book
def display_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            booklist = form.save()
            full_data = Book.objects.all()
            return render(request,'books.html',{
                'booklist':booklist ,
                'full_details':full_data          
            })
    else:
        form = BookForm()
    return render(request,'index.html',{'form':form})
