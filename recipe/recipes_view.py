from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .models import Recipes, Steps
from .forms import RecipeForm
import operator


def create_recipe(request):
    form = RecipeForm(request.POST or None)
    if request.method == 'POST':
        if request.user.is_authenticated():
            if form.is_valid():
                recipe_obj = form.save(commit=False)
                recipe_obj.owner = request.user.username
                recipe_obj.save()
                messages.success(request, 'Successfully Created a Recipe !!!', fail_silently=True)
                return HttpResponseRedirect(recipe_obj.get_absolute_url())
            else:
                messages.error(request, 'Failed to Create a Recipe!!!', fail_silently=True)
        else:
            messages.error(request, 'User should login to do this action!!', fail_silently=True)
    context = {'form': form}
    return render(request, 'myrecipe/recipe_form.html', context)


def delete_recipe(request, recipe_id):
    recipe_obj = get_object_or_404(Recipes, recipe_id=recipe_id)
    if request.user.is_authenticated():
        recipe_obj.delete()
        messages.success(request, 'Successfully Deleted a Recipe !!!', fail_silently=True)
    else:
        messages.error(request, 'Failed to Delete a Recipe !!! User should login to do this action.', fail_silently=True)
    return redirect('recipe:List_Recipe')


def update_recipe(request, recipe_id):
    recipe_obj = get_object_or_404(Recipes, recipe_id=recipe_id)
    form = RecipeForm(request.POST or None, instance=recipe_obj)
    if request.method == 'POST':
        if request.user.is_authenticated():
            if form.is_valid():
                recipe_obj = form.save(commit=False)
                recipe_obj.save()
                messages.success(request, 'Successfully Updated a Recipe !!!', fail_silently=True)
                return HttpResponseRedirect(recipe_obj.get_absolute_url())
            else:
                messages.error(request, 'Failed to Update a Recipe !!!', fail_silently=True)
        else:
            messages.error(request, 'User should login to do this action!!', fail_silently=True)
    context = {'title': recipe_obj.title,
               'recipe_obj': recipe_obj,
               'form': form}
    return render(request, 'myrecipe/recipe_form.html', context)


def list_recipe(request):
    if request.user.is_authenticated():
        page_id = 'recipe'
        recipes_list = Recipes.objects.filter(owner=request.user.username)

        query = request.GET.get('query')
        if query:
            recipes_list = recipes_list.filter(
                Q(title__icontains=query) |
                Q(owner__icontains=query) |
                Q(description__icontains=query)
            )
        paginator = Paginator(recipes_list, 6)  # Show 6 Recipes per page

        page = request.GET.get('page')
        try:
            query_set = paginator.page(page)
        except PageNotAnInteger:
            query_set = paginator.page(1)
        except EmptyPage:
            query_set = paginator.page(paginator.num_pages)

        return render(request, 'myrecipe/recipe.html', {'recipes_list': query_set, 'page_id': page_id})


def detail_recipe(request, recipe_id):
    recipe_obj = get_object_or_404(Recipes, recipe_id=recipe_id)
    steps = Steps.objects.filter(recipe=recipe_id)
    steps = sorted(steps, key=operator.attrgetter('number'))
    print steps
    context = {'title': recipe_obj.title,
               'recipe': recipe_obj,
               'steps_obj': steps
               }
    return render(request, 'myrecipe/detail_recipe.html', context)
