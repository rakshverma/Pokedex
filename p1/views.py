from django.shortcuts import render

def index(request):
    return render(request, 'index.html') 
def pokedex(request):
    return render(request, 'pokedex.html')
