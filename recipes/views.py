from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_list_or_404
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

    recipes = Recipe.objects.filter(
        is_published=True                                
    )
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
    
def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #     category__id=category_id,
    #     is_published=True  
    # ).order_by('-id')
    
    # if not recipes:
    #     raise Http404('Not Found 😓')
   
    # category_name = getattr(
    #     getattr(recipes.first(),'category', None),
    #     'name',
    #     'Not Found 404'
    # )
    
    # recipes = get_list_or_404(Recipe, category__id=category_id, is_published=True)
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id,
        is_published=True  
    ).order_by('-id'), category__id=category_id, is_published=True)
    
    print(recipes)
    return render(request,'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category',
    })
    
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_datails_page': True,
    })
