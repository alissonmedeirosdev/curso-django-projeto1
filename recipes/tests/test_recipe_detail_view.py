from django.urls import resolve,reverse
from recipes import views
from recipes.models import Recipe
from .test_recipe_base import RecipeTestBase

class RecipeDetailViewTest(RecipeTestBase):
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
    
    