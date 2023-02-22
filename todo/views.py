from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Todomodel

class TodoList(ListView):
    template_name = 'list.html'
    model = Todomodel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = Todomodel