from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# HTTP REQUEST 
def home(request):
    # HTTP RESPONSE
    # return HttpResponse('''
        
    #     <h1>
    #         Olá, Mundo!!
    #     </h1>                    
                        
    # ''') 
    
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Alisson Medeiros',
    })
    
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')
