from django import forms
from recipe.models import Recipe
from django.forms import ModelForm


# class RecipeForm(forms.Form):
#     recipe_name = forms.CharField(max_length = 150)
#     ingredients = forms.CharField(max_length = 220)
#     category = forms.CharField(max_length = 50)
#
#     def clean(self):
#         cleaned_data=super().clean()
#         recipename=cleaned_data.get('recipe_name')
#         recipe=Recipe.objects.filter(recipe_name=recipename)
#
#         if (recipe):
#             msg="This recipe already exists"
#             self.add_error('recipe_name',msg)

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe  # Recipe from models
        fields = "__all__"
        #   fields = ['recipe_name', 'ingredients', 'category']
        widgets={
            'recipe_name':forms.TextInput(attrs={'class':"form-control"}),
            'ingredients': forms.TextInput(attrs = {'class': "form-control"}),
            'category': forms.TextInput(attrs = {'class': "form-control"})
        }


    def clean(self):
        print("inside clean")

        cleaned_data = super().clean()
        recipename = cleaned_data.get('recipe_name')
        recipe = Recipe.objects.filter(recipe_name = recipename)

        if (recipe):
            msg = "This recipe already exists"
            self.add_error('recipe_name', msg)
