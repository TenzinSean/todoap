from django.urls import path

from .views import HomePageView, addTodo, deleteTodo


urlpatterns = [
    path('home/', HomePageView, name="home"),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
]
