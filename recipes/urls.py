from django.urls import path
from . import views


urlpatterns = [
    path('', views.home), # /HOME/
    path('recipes/<int:id>/', views.recipe), # /RECIPE/
]