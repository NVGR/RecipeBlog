from django.conf.urls import url

from . import step_view, recipes_view

urlpatterns = [
    url(r'^$', recipes_view.list_recipe, name='List_Recipe'),
    url(r'^create/$', recipes_view.create_recipe, name='Create_Recipe'),
    url(r'^(?P<recipe_id>\d+)/delete/$', recipes_view.delete_recipe, name='Delete_Recipe'),
    url(r'^(?P<recipe_id>\d+)/edit/$', recipes_view.update_recipe, name='Update_Recipe'),
    url(r'^(?P<recipe_id>\d+)/$', recipes_view.detail_recipe, name='Detail_Recipe'),
    url(r'^(?P<recipe_id>\d+)/createstep/$', step_view.create_step, name='Create_Step'),
    url(r'^(?P<step_id>\d+)/editstep/$', step_view.update_step, name='Update_Step'),
    url(r'^(?P<step_id>\d+)/deletestep/$', step_view.delete_step, name='Delete_Step'),
]

#<a href="{% url '' id=obj.id %}"></a>