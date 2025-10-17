from django.shortcuts import render
def emp(request):
    my_objects = [
        {'name': 'Salman', 'job_title': 'Developer', 'salary': 15000, 'full_time': True},
        {'name': 'Alfariz', 'job_title': 'Designer', 'salary': 15000, 'full_time': True},
        {'name': 'Ashik', 'job_title': 'Manager', 'salary': 15000, 'full_time': False},
        {'name': 'Samiya', 'job_title': 'Developer', 'salary': 15000, 'full_time': True},
        {'name': 'Vishnu', 'job_title': 'Designer', 'salary': 15000, 'full_time': True},
        {'name': 'Adhithyan', 'job_title': 'Manager', 'salary': 15000, 'full_time': False}
    ]
    context = {'my_objects': my_objects}
    return render(request, 'home.html', context)
