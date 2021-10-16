from django.core.exceptions import ValidationError
from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ToDoSerializer 
from .models import ToDo
from todo import serializers


class ToDoList(generics.ListAPIView):
    queryset = ToDo.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ToDoSerializer 

    def get_queryset(self):
        return ToDo.objects.filter(creator=self.request.user)

class ToDoCreate(generics.CreateAPIView):
    serializer_class = ToDoSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ToDoRetrieve(generics.RetrieveAPIView):
    serializer_class = ToDoSerializer 
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(pk=self.kwargs['pk'], creator=self.request.user)


class ToDoUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = ToDoSerializer 
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return ToDo.objects.filter(pk=self.kwargs['pk'])
    

class ToDoDestroy(generics.DestroyAPIView):
    serializer_class = ToDoSerializer 
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return ToDo.objects.filter(pk=self.kwargs['pk'], creator=self.request.user)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('This is not your todo.')

    
