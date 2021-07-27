from django.shortcuts import render, redirect
from django.http import HttpResponse
from collections import Counter





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
        # print(title)


        #  Grabbing first 2 words from product name 
        mainTitle = []
        for name in title:
            splitTitle = name.replace("'", "").split(' ')
            joined = " ".join(splitTitle[0:2])
            mainTitle.append(joined)
        # print(mainTitle)








  
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
        # print(ingredientCount)


        inglist = zip(ing1, ing2, ing3, ing4)

        # Works out the most common ingredients across all products , the more frequent a specific ingredients comes in a list the higher the percentage in the pie chart
        common1 = []
        if len(ing3) < 1:
            for item in match1_2:
                common1.append(item)
            common_count = Counter(common1)
            prod_name = []
            count_value = []
            for key, value in common_count.items():
                prod_name.append(key)
                count_value.append(value)
            # print(common_count)
        # print(common1)

        common2 = []
        if len(ing3) > 1 and len(ing4) < 1:
            for item1 in match1_2:
                common2.append(item1)
            for item2 in match1_3:
                common2.append(item2)
            for item3 in match2_3:
                common2.append(item3)
            for item4 in All_1_2_3:
                common2.append(item4)
            common_count = Counter(common2)
            prod_name = []
            count_value = []
            for key, value in common_count.items():
                prod_name.append(key)
                count_value.append(value)
        # print(common2)

        common3 = []
        if len(ing4) > 1:
            for item1 in match1_2:
                common3.append(item1)
            for item2 in match1_3:
                common3.append(item2)  
            for item3 in match1_4:
                common3.append(item3)  
            for item4 in match2_3:
                common3.append(item4)  
            for item5 in match2_4:
                common3.append(item5)  
            for item6 in match3_4:
                common3.append(item6)  
            for item7 in All_1_2_3_4:
                common3.append(item7)  

            common_count = Counter(common3)
            prod_name = []
            count_value = []
            for key, value in common_count.items():
                prod_name.append(key)
                count_value.append(value)
            # print(common_count)
            
        # print(common3)


        


        # Different contexts depending on how many instances of compare forms there are in the compare html page 
        if len(ing3) < 1:

            context0 = {
                'ing1': ing1,
                'ing2': ing2,
                'inglist': inglist,
                'match1_2': match1_2,
                'title': title,
                'ingredientCount': ingredientCount,
                'mainTitle': mainTitle,
                'prod_name': prod_name,
                'count_value': count_value,
                'ing1list': ing1list,
                'ing2list': ing2list,
                'ing3list': ing3list,
                'ing4list': ing4list,
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
                'mainTitle': mainTitle,
                'prod_name': prod_name,
                'count_value': count_value,
                'ing1list': ing1list,
                'ing2list': ing2list,
                'ing3list': ing3list,
                'ing4list': ing4list,
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
                'mainTitle': mainTitle,
                'prod_name': prod_name,
                'count_value': count_value,
                'ing1list': ing1list,
                'ing2list': ing2list,
                'ing3list': ing3list,
                'ing4list': ing4list,
            }

            return render(request, 'result/results.html', context2)
        

    return render(request, 'result/compare.html')








