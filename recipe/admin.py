from django.contrib import admin
from .models import Recipes, Steps


class RecipesModelAdmin(admin.ModelAdmin):
    list_display = ["title", "owner"]
    list_display_links = ["title"]
    list_filter = ["title", "owner"]
    search_fields = ["title", "description"]

    class Meta:
        model = Recipes

admin.site.register(Recipes, RecipesModelAdmin)


class StepsModelAdmin(admin.ModelAdmin):
    list_display = ["step_id", "owner"]
    list_display_links = ["step_id"]
    list_filter = ["number", "owner"]
    search_fields = ["owner", "description"]

    class Meta:
        model = Recipes

admin.site.register(Steps, StepsModelAdmin)
