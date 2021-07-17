from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'result/home.html')



def compare_ingredients(request):
    if request.method == "POST":

        ingredients1 = request.POST.get('ingredients1')
        ingredients2 = request.POST.get('ingredients2')

        print(ingredients1, ingredients2)

    return render(request, 'result/compare.html')



