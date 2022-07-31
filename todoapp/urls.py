from django.urls import path
from .views import HomeView, todo_item_delete,todo_list_view,todo_item_create,todo_item_delete



app_name='todoapp'
urlpatterns = [
    path('',HomeView,name='home'),
    path('list/',todo_list_view,name='todo_list'),
    path('create/',todo_item_create,name='todo_item_create'),
    path('<id>/delete',todo_item_delete,name='todo_item_delete'),

]
