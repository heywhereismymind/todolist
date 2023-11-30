from . import views
from django.urls import path, re_path

urlpatterns = [
    path('tasks', views.todolist_list),
    re_path(r'^tasks/(?P<pk>[0-9]+)$', views.to_do_list_detail)

]
