from django.shortcuts import render



def home(request):
    return render(request, 'result/home.html')



def compare_ingredients(request):
    if request.method == "POST":
        ingredients = request.POST['ingredients']
        
        for item in ingredients.split(','):
            print(item)

    return render(request, 'result/compare.html')
