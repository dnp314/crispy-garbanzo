from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderIteminline(admin.TabularInline):
  model = OrderItem

class OrderAdmin(admin.ModelAdmin):
  inlines =[
    OrderIteminline
  ]

admin.site.register(Order, OrderAdmin)