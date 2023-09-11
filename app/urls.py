
from django.urls import re_path,path
from . import views

urlpatterns = [
    re_path(r'^/(?P<id>\d+)$',views.handle_person),
    path("",views.create_view)
]