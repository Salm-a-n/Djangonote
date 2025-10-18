from django.shortcuts import render

def greeting(request):
    if request.GET:
        name = request.GET.get('username')
        form_data = request.GET  # This contains all GET parameters
        return render(request, 'output.html', {
            'name': name,
            'form_data': form_data,
        })
    return render(request, 'input.html')
