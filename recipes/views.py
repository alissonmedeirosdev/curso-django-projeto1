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
    
    return render(request, 'recipes/home.html', context={
        'name': 'Alisson Medeiros',
    })

def contato(request):
    return HttpResponse('Página de contato')

def sobre(request):
    return HttpResponse('Página sobre')