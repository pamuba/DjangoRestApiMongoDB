from django.urls import re_path as url
from demos import views 
 
urlpatterns = [ 
    url(r'^api/demos$', views.tutorial_list),
    url(r'^api/demos/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/demos/published$', views.tutorial_list_published)
]