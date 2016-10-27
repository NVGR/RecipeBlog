from django import forms
from .models import Recipes, Steps


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = [
            "title",
            "description"
        ]


class StepsForm(forms.ModelForm):
    class Meta:
        model = Steps
        fields = [
            "number",
            "description",
        ]