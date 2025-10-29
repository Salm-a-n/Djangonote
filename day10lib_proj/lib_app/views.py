from django.shortcuts import render, redirect
from .forms import lib_form
from.models import Lib_manage
from django.core.paginator import Paginator
def create_book(request):
    if request.method == 'POST':
        form = lib_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =lib_form()
    return render(request, 'lib_app/index.html', {'form': form})
def all_data (request):
    book_list = Lib_manage.objects.all()
    paginator = Paginator(book_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lib_app/all_result.html', {'book_list': page_obj.object_list, 'page_obj': page_obj})

def update_book(request, id):
    book = Lib_manage.objects.get(pk=id) 
    if request.method == 'POST':
        form = lib_form(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =lib_form(instance=book)           
    return render(request, 'lib_app/update.html', {'form': form})
def delete_book(request,title):
    book=Lib_manage.objects.get(title=title)  
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    
    return render(request,'lib_app/delete.html',{'book':book})
