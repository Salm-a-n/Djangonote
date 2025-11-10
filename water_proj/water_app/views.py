from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.utils import timezone
from django.contrib import messages
from .forms import WaterIntakeForm,DateRangeForm
from .models import WaterIntakeModel
from django.core.paginator import Paginator
def home(request):
    return render(request,'waterapp/home.html')
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'waterapp/signup.html', {'form': form})

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'waterapp/login.html', {'form': form})

@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'waterapp/logout.html', context)


@login_required(login_url='/login/')
def add_water(request):
    today = timezone.now().date()
    already_added = WaterIntakeModel.objects.filter(user=request.user, date=today).exists()
    if already_added:
        return render(request, 'waterapp/addwater.html',{'messages': "You've already added your intake for today."})

    if request.method == 'POST':
        form = WaterIntakeForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Water intake added successfully!")
            return redirect('waterlist')
    else:
        form = WaterIntakeForm(user=request.user)

    return render(request, 'waterapp/addwater.html', {'form': form})


@login_required(login_url='/login/')
def waterlist(request):
    intakes = WaterIntakeModel.objects.filter(user=request.user).order_by('-date')
    paginator = Paginator(intakes,1) 
    page = request.GET.get('page')
    intakes_page = paginator.get_page(page)
    return render(request, 'waterapp/waterlist.html', {'intakes': intakes_page})


@login_required(login_url='/login/')
def edit_intake(request, pk):
    intake = get_object_or_404(WaterIntakeModel, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WaterIntakeForm(request.POST, instance=intake, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Intake updated.")
            return redirect('waterlist')
    else:
        form = WaterIntakeForm(instance=intake, user=request.user)  
    return render(request, 'waterapp/editwater.html', {'form': form})

@login_required(login_url='/login/')
def delete_intake(request, pk):
    intake = get_object_or_404(WaterIntakeModel, pk=pk, user=request.user)
    if request.method == 'POST':
        intake.delete()
        messages.success(request, "Intake deleted.")
        return redirect('waterlist')
    return render(request, 'waterapp/deletewater.html', {'intake': intake})

@login_required(login_url='/login/')
def intake_difference(request):
    result = None
    status=None
    data = WaterIntakeModel.objects.filter(user=request.user).exists()
    if not data:
        messages.error(request, "You haven't added any water intake yet. you can add water intake here ")
        return redirect('addwater')


    form = DateRangeForm(user=request.user)

    if request.method == 'POST':
        form = DateRangeForm(request.POST, user=request.user)
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']
            
            
            if start == end:
                messages.error(request, "You are selecting the same date. Please choose two different dates.You can see what dates are available in the All List in the navbar ")
                return redirect('intake_difference')
            start_entry = WaterIntakeModel.objects.filter(user=request.user, date=start).first()
            end_entry = WaterIntakeModel.objects.filter(user=request.user, date=end).first()
            
            result = abs(end_entry.quantity - start_entry.quantity)
            if end_entry.quantity < start_entry.quantity:
                status = "Your water intake was decreased"
            elif end_entry.quantity > start_entry.quantity:
                status = "Good! Your water intake was increased"
            else:
                status =" same intake"



    return render(request, 'waterapp/intakedifference.html', {'form': form, 'result': result,'status':status})

