from django.shortcuts import render
from .forms import IngredientsForm



def home(request):
    return render(request, 'result/home.html')



def compare_ingredients(request):
    if request.method == "POST":
        form1 = IngredientsForm(request.POST)
        form2 = IngredientsForm(request.POST)
        
        if form1.is_valid():
            data = form1.save(commit=False)
            data.save()
        if form2.is_valid():
            data = form2.save(commit=False)
            data.save()
    else:
        form1 = IngredientsForm()
        form2 = IngredientsForm()
    
    context = {
        'form1': form1,
        'form2': form2,

    }
        
    return render(request, 'result/compare.html', context)
