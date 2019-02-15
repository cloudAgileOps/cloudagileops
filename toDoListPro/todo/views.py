# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from todo.models import List

# Create your views here.

def status_report(request):  
  todo_listing = []  
  for todo_list in List.objects.all():  
    todo_dict = {}  
    todo_dict['list_object'] = todo_list  
    todo_dict['item_count'] = todo_list.item_set.count()  
    todo_dict['items_complete'] = todo_list.item_set.filter(completed=True).count()  
    if todo_dict['item_count'] == 0: 
        todo_dict['percent_complete'] = 'NULL'
    else:
        todo_dict['percent_complete'] =  str(int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100)) + '%'  
    todo_listing.append(todo_dict)  
  return render(request, 'status_report.html', { 'todo_listing': todo_listing })
