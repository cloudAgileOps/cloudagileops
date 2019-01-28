# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from todo.models import List
from todo.models import Item 
admin.site.register(Item)
admin.site.register(List)
