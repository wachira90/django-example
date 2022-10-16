from django.contrib import admin

# Register your models here.
from .models import Task, Product, Customer, Place, Restaurant, Waiter

# Register our model
admin.site.register(Task)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)