from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Todomodel

class TodoList(ListView):
    template_name = 'list.html'
    model = Todomodel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = Todomodel

class TodoCreate(CreateView):
  template_name = 'create.html'
  model = Todomodel
  fields = ('title', 'memo', 'duedate', 'priority')
  success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
   template_name = 'delete.html'
   model = Todomodel
   success_url = reverse_lazy('list')