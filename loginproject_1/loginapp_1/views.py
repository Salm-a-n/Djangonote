from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form['email'].value
            return render(request, 'thankyou.html', {'email': email})
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

# Create your views here.
