from django.shortcuts import render, redirect
from django.http import HttpResponse



def home(request):
    return render(request, 'result/home.html')



def compare_ingredients(request):

    if request.method == 'POST':

        ing1 = request.POST.getlist('ingredients1')
        ing2 = request.POST.getlist('ingredients2')
        ing3 = request.POST.getlist('ingredients3')
        ing4 = request.POST.getlist('ingredients4')
        ing5 = request.POST.getlist('ingredients5')
        ing6 = request.POST.getlist('ingredients6')
        ing7 = request.POST.getlist('ingredients7')
        ing8 = request.POST.getlist('ingredients8')
        ing9 = request.POST.getlist('ingredients9')
        ing10 = request.POST.getlist('ingredients10')

        ing1list = []
        for ele in ing1[1:]:
            ele_split = ele.split(",")
            for ele2 in ele_split:
                ing1list.append(ele2.strip().lower())

        print(ing1list)



    
        context = {
            'ing1': ing1,
            'ing2': ing2,
            'ing3': ing3,
            'ing4': ing4,
            'ing5': ing5,
            'ing6': ing6,
            'ing7': ing7,
            'ing8': ing8,
            'ing9': ing9,
            'ing10': ing10,
        }



        return render(request, 'result/results.html', context)
        

    return render(request, 'result/compare.html')








