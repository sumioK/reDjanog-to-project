from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Todomodel
class TodoList(ListView):
    template_name = 'list.html'
    model = Todomodel
