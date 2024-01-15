from django.shortcuts import render

def search(request):
    return render(request, 'products/search.html')

def display_results(request):
    pass