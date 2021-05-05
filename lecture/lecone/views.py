from django.shortcuts import render

def home(request):
    return render(request, 'lecone/blog.html')

def about(request):
    return render(request, 'lecone/lect.html')