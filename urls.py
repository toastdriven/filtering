from django.conf.urls.defaults import patterns, include, url


from tastypie.api import Api
from filterme.api import ParentResource, ChildResource

v1_api = Api()
v1_api.register(ParentResource())
v1_api.register(ChildResource())


urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)
