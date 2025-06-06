from django.urls import resolve,reverse
from recipes import views
from recipes.models import Recipe
from .test_recipe_base import RecipeTestBase

class RecipeHomeViewTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_return_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home')) 
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_templete(self):
        response = self.client.get(reverse('recipes:home')) 
        self.assertTemplateUsed(response, 'recipes/pages/home.html')  

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home')) 
        self.assertIn(
            '<h1>Not recipes found here 😓</h1>',
            response.content.decode('utf-8')
        ) 

    def test_recipe_home_templete_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_context_recipes = response.context['recipes']
        content = response.content.decode('utf-8')

        self.assertIn('Recipe title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_templete_dont_load_recipes_not_published(self):
        """
            Test recipe is published False dont show
        """
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8') 
        
        self.assertIn(
            '<h1>Not recipes found here 😓</h1>',
            content
        ) 

   
        url = reverse('recipes:search') + '?q=test'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;test&quot;',
            response.content.decode('utf-8')
        )