from django.shortcuts import render




def home(request):
    return render(request, 'result/home.html')



def compare_ingredients(request):
        
        
    return render(request, 'result/compare.html')
