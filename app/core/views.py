from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['filename']
        print(uploaded_file.name)
    return render(request, 'registration.html')

