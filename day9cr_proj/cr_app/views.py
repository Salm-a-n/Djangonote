from django.shortcuts import render
student_list = {
    'Ali': {'Math': 85, 'Science': 90, 'English': 88},
    'Sara': {'Math': 92, 'Science': 95, 'English': 89},
    'John': {'Math': 78, 'Science': 80, 'English': 82},
}

def index(request):
    students = list(student_list.keys())
    return render(request, 'index.html', {'students': students})

def show_result(request, student_name):
    result = student_list.get(student_name)
    return render(request, 'result.html', {'name': student_name, 'result': result})