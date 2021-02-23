from django.shortcuts import render

# Create your views here.
def frogger(request):
    return render(request, 'frogger.html')

def pacman(request):
    return render(request, 'pacman.html')
