from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from recipe.models import Recipes


class HomeView(TemplateView):
    template_name = 'myrecipe/index.html'
    page_id = 'home'

    def get(self, request, *args, **kwargs):
        recipes_list = Recipes.objects.all()

        # Search functionality
        query = request.GET.get('query')
        if query:
            recipes_list = recipes_list.filter(
                Q(title__icontains=query) |
                Q(owner__icontains=query) |
                Q(description__icontains=query)
            )

        # Pagination Code
        paginator = Paginator(recipes_list, 6)  # Show 6 Recipes per page
        page = request.GET.get('page')
        try:
            query_set = paginator.page(page)
        except PageNotAnInteger:
            query_set = paginator.page(1)
        except EmptyPage:
            query_set = paginator.page(paginator.num_pages)

        context = {'recipes_list': query_set, 'page_id': self.page_id}

        return render(request, self.template_name, context)
