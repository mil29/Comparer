from django.shortcuts import render, redirect
from django.http import HttpResponse



def home(request):
    return render(request, 'result/home.html')



def compare_ingredients(request):

    if request.method == 'POST':

        # get data from textareas in form 
        ing1 = request.POST.getlist('ingredients1')
        ing2 = request.POST.getlist('ingredients2')
        ing3 = request.POST.getlist('ingredients3')
        ing4 = request.POST.getlist('ingredients4')

        #  create eempty lists to contain data from each form
        ing1list = []
        ing2list = []
        ing3list = []
        ing4list = []

        #  Here each request.POST is looped through and a set for each is created  


        #  loop through request.POST starting from element 1 , clean up using split, strip and lower then adding to list
        for ele in ing1[1:]:
            ele_split = ele.split(",")
            for ele2 in ele_split:
                ing1list.append(ele2.strip().lower())
        
        #  create a Set from list created in function above 
        set1 = set(ing1list)
        # print(set1)

        for ele in ing2[1:]:
            ele_split = ele.split(",")
            for ele2 in ele_split:
                ing2list.append(ele2.strip().lower())
        
        set2 = set(ing2list)
        # print(set2)

        for ele in ing3[1:]:
            ele_split = ele.split(",")
            for ele2 in ele_split:
                ing3list.append(ele2.strip().lower())

        set3 = set(ing3list)
        # print(set3)

        for ele in ing4[1:]:
            ele_split = ele.split(",")
            for ele2 in ele_split:
                ing4list.append(ele2.strip().lower())

        set4 = set(ing4list)


        if len(set2) >= 1 and len(set3) < 1:
            match1 = set1.intersection(set2)
            print(f'Item 1 and Item 2 both have: {match1}')

        if len(set3) >= 1 and len(set4) < 1:
            match1 = set1.intersection(set2)
            match2 = set1.intersection(set3)
            match3 = set2.intersection(set3)
            All = set.intersection(set1, set2, set3)
            print(f'Item 1 and Item 2 both have: {match1}')
            print(f'Item 1 and Item 3 both have: {match2}')
            print(f'Item 2 and Item 3 both have: {match3}')
            print(f'All Items have: {All}')

        if len(set4) >= 1:
            match1 = set1.intersection(set2)
            match2 = set1.intersection(set3)
            match3 = set1.intersection(set4)
            match4 = set2.intersection(set3)
            match5 = set2.intersection(set4)
            match6 = set3.intersection(set4)
            All    = set.intersection(set1, set2, set3, set4)
            print(f'Item 1 and Item 2 both have: {match1}')
            print(f'Item 1 and Item 3 both have: {match2}')
            print(f'Item 1 and Item 4 both have: {match3}')
            print(f'Item 2 and Item 3 both have: {match4}')
            print(f'Item 2 and Item 4 both have: {match5}')
            print(f'Item 3 and Item 4 both have: {match6}')
            print(f'All Items have: {All}')


        inglist = zip(ing1, ing2, ing3, ing4)
        
        context = {
            'ing1': ing1,
            'ing2': ing2,
            'ing3': ing3,
            'ing4': ing4,
            'inglist': inglist,
        }


        return render(request, 'result/results.html', context)
        

    return render(request, 'result/compare.html')








