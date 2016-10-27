from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Steps, Recipes
from .forms import StepsForm
from django.contrib import messages


def create_step(request, recipe_id):
    form = StepsForm(request.POST or None)

    if request.method == 'POST':
        if request.user.is_authenticated():
            if form.is_valid():
                step_obj = form.save(commit=False)
                step_obj.owner = request.user.username
                step_obj.recipe_id = recipe_id
                step_obj.save()
                recipe_obj = Recipes.objects.get(recipe_id=recipe_id)
                messages.success(request, 'Successfully Created a Step !!!', fail_silently=True)
                return HttpResponseRedirect(recipe_obj.get_absolute_url())
            else:
                messages.error(request, 'Failed to Create a Step!!!', fail_silently=True)
        else:
            messages.error(request, 'User should login to do this action!!', fail_silently=True)
    context = {'form': form}
    return render(request, 'myrecipe/step_form.html', context)


def delete_step(request, step_id):
    step_obj = get_object_or_404(Steps, step_id=step_id)
    if request.user.is_authenticated():
        step_obj.delete()
        messages.success(request, 'Successfully Deleted a Step !!!', fail_silently=True)
    else:
        messages.error(request, 'Failed to Delete a Step !!! User should login to do this action.', fail_silently=True)
    recipe_obj = get_object_or_404(Recipes, recipe_id=step_obj.recipe.recipe_id)
    print '**** {0}'.format(recipe_obj.title)
    return HttpResponseRedirect(recipe_obj.get_absolute_url())


def update_step(request, step_id):
    step_obj = get_object_or_404(Steps, step_id=step_id)
    form = StepsForm(request.POST or None, instance=step_obj)
    if request.method == 'POST':
        if request.user.is_authenticated():
            if form.is_valid():
                step_obj = form.save(commit=False)
                step_obj.save()
                messages.success(request, 'Successfully Updated a Step !!!', fail_silently=True)
                recipe_obj = get_object_or_404(Recipes, recipe_id=step_obj.recipe.recipe_id)
                print '**** {0}'.format(recipe_obj.title)
                return HttpResponseRedirect(recipe_obj.get_absolute_url())
            else:
                messages.error(request, 'Failed to Update a Step !!!', fail_silently=True)
        else:
            messages.error(request, 'User should login to do this action!!', fail_silently=True)
    context = {'title': step_obj.number,
               'step_obj': step_obj,
               'form': form}
    return render(request, 'myrecipe/step_form.html', context)
