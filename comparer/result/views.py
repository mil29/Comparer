from django.shortcuts import render, redirect
from django.http import HttpResponse





def home(request):
    return render(request, 'result/home.html')



def compare(request):


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


        #  data for the charts to get the title name of product for the labels array in chart.js
        title = []
        for item in ing1[0:1]:
            title.append(item)
        for item in ing2[0:1]:
            title.append(item)
        for item in ing3[0:1]:
            title.append(item)
        for item in ing4[0:1]:
            title.append(item)
        print(title)








  
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
            match1_2 = set1.intersection(set2)
            # print(f'Item 1 and Item 2 both have: {match1_2}')

        if len(set3) >= 1 and len(set4) < 1:
            match1_2 = set1.intersection(set2)
            match1_3 = set1.intersection(set3)
            match2_3 = set2.intersection(set3)
            All_1_2_3 = set.intersection(set1, set2, set3)
            # print(f'Item 1 and Item 2 both have: {match1_2}')
            # print(f'Item 1 and Item 3 both have: {match1_3}')
            # print(f'Item 2 and Item 3 both have: {match2_3}')
            # print(f'All Items have: {All_1_2_3}')

        if len(set4) >= 1:
            match1_2 = set1.intersection(set2)
            match1_3 = set1.intersection(set3)
            match1_4 = set1.intersection(set4)
            match2_3 = set2.intersection(set3)
            match2_4 = set2.intersection(set4)
            match3_4 = set3.intersection(set4)
            All_1_2_3_4    = set.intersection(set1, set2, set3, set4)
            # print(f'Item 1 and Item 2 both have: {match1_2}')
            # print(f'Item 1 and Item 3 both have: {match1_3}')
            # print(f'Item 1 and Item 4 both have: {match1_4}')
            # print(f'Item 2 and Item 3 both have: {match2_3}')
            # print(f'Item 2 and Item 4 both have: {match2_4}')
            # print(f'Item 3 and Item 4 both have: {match3_4}')
            # print(f'All Items have: {All_1_2_3_4}')


        #  for charts to count total number of ingredients in each product for the data array in chart.js
        ingredientCount = []
        ingredientCount.append(len(ing1list))
        ingredientCount.append(len(ing2list))
        if len(ing3list) > 1:         
            ingredientCount.append(len(ing3list))
        if len(ing4list) > 1:
            ingredientCount.append(len(ing4list))
        print(ingredientCount)


        inglist = zip(ing1, ing2, ing3, ing4)

    
        if len(ing3) < 1:

            context0 = {
                'ing1': ing1,
                'ing2': ing2,
                'inglist': inglist,
                'match1_2': match1_2,
                'title': title,
                'ingredientCount': ingredientCount,
            }

            return render(request, 'result/results.html', context0)
        
        if len(ing3) > 1 and len(ing4) < 1:

            context1 = {
                'ing1': ing1,
                'ing2': ing2,
                'ing3': ing3,
                'inglist': inglist,
                'match1_2': match1_2,
                'match1_3': match1_3,
                'match2_3': match2_3,
                'All_1_2_3': All_1_2_3,
                'title': title,
                'ingredientCount': ingredientCount,
            }

            return render(request, 'result/results.html', context1)
        
        if len(ing4) > 1:

            context2 = {
                'ing1': ing1,
                'ing2': ing2,
                'ing3': ing3,
                'ing4': ing4,
                'inglist': inglist,
                'match1_2': match1_2,
                'match1_3': match1_3,
                'match2_3': match2_3,
                'match1_4': match1_4,
                'match2_4': match2_4,
                'match3_4': match3_4,
                'All_1_2_3_4': All_1_2_3_4,
                'title': title,
                'ingredientCount': ingredientCount,
            }

            return render(request, 'result/results.html', context2)
        

    return render(request, 'result/compare.html')








