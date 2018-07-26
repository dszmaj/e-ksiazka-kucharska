from django.shortcuts import render_to_response, render


def root(request):
    return render_to_response('index.html')


def dashboard(request):
    return render(request, 'index.html', {'dashboard': dashboard})
