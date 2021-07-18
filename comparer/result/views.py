from django.shortcuts import render, redirect
from django.http import HttpResponse



def home(request):
    return render(request, 'result/home.html')



def compare_ingredients(request):



    ingredients1 = request.POST.getlist('ingredients1')
    ingredients2 = request.POST.getlist('ingredients2')
    ingredients3 = request.POST.getlist('ingredients3')
    ingredients4 = request.POST.getlist('ingredients4')
    ingredients5 = request.POST.getlist('ingredients5')
    ingredients6 = request.POST.getlist('ingredients6')
    ingredients7 = request.POST.getlist('ingredients7')
    ingredients8 = request.POST.getlist('ingredients8')
    ingredients9 = request.POST.getlist('ingredients9')
    ingredients10 = request.POST.getlist('ingredients10')

    if len(ingredients1) >= 1:


        return redirect('results')
        

    return render(request, 'result/compare.html')




def results(request):
    ingredients1 = request.POST.getlist('ingredients1')

    context = {
        'ingredients1': ingredients1,
    }


    return render(request, 'result/results.html', context)






