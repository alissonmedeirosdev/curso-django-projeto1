from .test_recipe_base import RecipeTestBase

class RecipeCategoryModelTest(RecipeTestBase):
    def setUp(self):
        self.category = self.meke_category(
            name='Testing Category'
        )
        return super().setUp()
    
    def test_recipe_category_model_string_representation(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )
    
   