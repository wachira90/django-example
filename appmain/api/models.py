from django.db import models

# Create your models here.
# from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(default="-")
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        db_table = 'task'
    
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    id_code = models.CharField(max_length=100)
    description = models.TextField(default="-")
    price1 = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)   #max_digits=5, decimal_places=2  = 999.99
    price2 = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)   #
    # price1 = models.IntegerField(default=0)
    # price2 = models.IntegerField(default=0)
    supplier = models.CharField(max_length=100,default=0)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        db_table = 'product'
    
    def __str__(self):
        return "%s # %s # %s" % (self.title, self.price1, self.price2)
        # return self.title


class Customer(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    tel1 = models.CharField(max_length=10)
    tel2 = models.CharField(max_length=10)
    description = models.TextField(default="-")
    invite_code = models.CharField(max_length=50, default=0)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        db_table = 'customer'
    
    def __str__(self):
        return self.firstname         


# =====================
# 


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
    is_active = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        db_table = 'place'

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        db_table = 'restaurant'

    def __str__(self):
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        db_table = 'waiter'

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)