from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/create', views.ToDoCreate.as_view()),
    path('api/todos/<int:pk>', views.ToDoRetrieve.as_view()),
    path('api/todos', views.ToDoList.as_view()),
    path('api/todos/<int:pk>/delete', views.ToDoDestroy.as_view()),
    path('api/todos/<int:pk>/update', views.ToDoUpdate.as_view()),
]
