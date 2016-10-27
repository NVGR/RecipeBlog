from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


class Recipes(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    owner = models.CharField(max_length=50, null=False, blank=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    # step = models.ManyToManyField(Steps)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipe:Detail_Recipe", kwargs={'recipe_id': self.recipe_id})

    class Meta:
        ordering = ['-timestamp', '-updated']


class Steps(models.Model):
    step_id = models.AutoField(primary_key=True)
    number = models.IntegerField(default=1)
    description = models.TextField(null=False, blank=False)
    owner = models.CharField(max_length=50, null=False, blank=False)
    #recipe = models.ManyToManyField(Recipes)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    def __unicode__(self):
        return '{0}'.format(self.step_id)
