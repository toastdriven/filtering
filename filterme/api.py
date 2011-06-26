from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from filterme.models import Parent, Child


class ParentResource(ModelResource):
    class Meta:
        queryset = Parent.objects.all()
        filtering = {
            'name': ALL,
        }


class ChildResource(ModelResource):
    parents = fields.ToManyField(ParentResource, 'parents')
    
    class Meta:
        queryset = Child.objects.all()
        filtering = {
            'parents': ALL_WITH_RELATIONS,
            'first_name': ALL,
        }
