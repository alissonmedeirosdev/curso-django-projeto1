from django.urls import resolve,reverse
from recipes import views
from recipes.models import Recipe
from .test_recipe_base import RecipeTestBase

class RecipeViewsTest(RecipeTestBase):

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

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_categoty_view_return_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000})) 
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_templete_loads_recipes(self):
        needed_title = 'This is a category test'

        self.make_recipe(title=needed_title)
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_category_templete_dont_load_recipes_not_published(self):
        """
            Test recipe is published False dont show
        """
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.category.id})) 
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)
    
    def test_recipe_detail_view_return_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000})) 
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_templete_loads_the_correct_recipes(self):
        needed_title = 'This is a detail page - It load one recipe'

        self.make_recipe(title=needed_title)
        response = self.client.get(
            reverse(
                'recipes:recipe', 
                kwargs={
                    'id': 1
                }
            )
        )
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_detail_templete_dont_load_recipes_not_published(self):
        """
            Test recipe is published False dont show
        """
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': recipe.id})) 
        self.assertEqual(response.status_code, 404)
    
    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)

    def test_recipe_search_loads_correct_templete(self):
        response = self.client.get(reverse('recipes:search') + '?q=test')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

