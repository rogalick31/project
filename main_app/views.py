from django.shortcuts import render

def index(request):
    """Головна сторінка "Журналу спостережень" """
    return render(request, 'main_app/index.html')
