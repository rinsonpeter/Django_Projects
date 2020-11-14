from django.shortcuts import render, redirect
# Create your views here.
from recipe.forms import RecipeForm
from recipe.models import Recipe


def createRecipe(request):
    print("inside create recipe")
    template_name = "createrecipe.html"

    context = {}
    context['form'] = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            print("inside is valid")
            form.save()
            # recipe_name = form.cleaned_data.get('recipe_name')# ingredients = form.cleaned_data.get('ingredients')# category = form.cleaned_data.get('category')# obj = Recipe(recipe_name = recipe_name,#              ingredients = ingredients,  #              category    = category)# obj.save()

            return redirect("listrecipe")
        else:
            context['form'] = form
            return render(request, template_name, context)

    return render(request, template_name, context)


def listrecipe(request):
    template_name = 'listrecipe.html'
    qs = Recipe.objects.all()
    context = {}
    context['recipes'] = qs
    return render(request, template_name, context)


def viewrecipe(request, pk):
    template_name = 'viewrecipe.html'
    qs = Recipe.objects.get(id = pk)
    context = {}
    context['recipe'] = qs
    return render(request, template_name, context)


def deleterecipe(request, pk):
    qs = Recipe.objects.get(id = pk).delete()
    return redirect("listrecipe")


def updaterecipe(request, pk):
    recipe = Recipe.objects.get(id = pk)
    form = RecipeForm(instance = recipe)
    context = {}
    context['form'] = form

    if request.method == 'POST':
        form = RecipeForm(instance = recipe, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('listrecipe')

    return render(request, 'recipeupdate.html', context)
