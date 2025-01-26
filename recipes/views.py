from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe
# Create your views here.

# HTTP REQUEST 
def home(request):
    # HTTP RESPONSE
    # return HttpResponse('''
        
    #     <h1>
    #         Olá, Mundo!!
    #     </h1>                    
                        
    # ''') 

    recipes = Recipe.objects.all().order_by('-id')
    print(recipes)
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
    
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_datails_page': True,
    })
