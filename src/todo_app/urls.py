from django.urls import path

from .views import index, add_todo, delete_todo

app_name="todo_app"

urlpatterns = [
    path('', index, name="index"),
    path('add_todo/', add_todo, name="add_todo"),
    path('delete_todo/<int:item_id>', delete_todo, name="delete_todo")
]
