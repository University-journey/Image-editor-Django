# urls.py
from django.urls import path
from . import views

# "" is root of website.
# urlpatterns = [
#     path("", views.home, name="home"),
#     path("todos/", views.todos, name="todos")
# ]
urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('image/<int:id>/', views.image_detail, name='image_detail'),
]
