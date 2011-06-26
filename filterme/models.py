from django.db import models


class Parent(models.Model):
    name = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.name


class Child(models.Model):
    parents = models.ManyToManyField(Parent, related_name='children')
    first_name = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.first_name
