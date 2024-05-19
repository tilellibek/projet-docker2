from django.shortcuts import render



def index(request):
    return render(request, 'infos/index.html', {})

def formations(request):
    return render(request, 'infos/courses.html', {})

def about(request):
    return render(request, 'infos/about.html', {})

def contact(request):
    return render(request, 'infos/contact.html', {})