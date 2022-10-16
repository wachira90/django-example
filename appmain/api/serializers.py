from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task, Customer, Product, Place, Restaurant, Waiter

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

'''
HOME AUTH SECTION 
'''

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'complete', 'date_created', 'date_update')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'firstname', 'lastname','email','tel1','tel2','description','invite_code', 'is_active', 'date_created','date_update')	


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'id_code','description', 'price1','price2','supplier','is_active', 'date_created','date_update')	                


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'address', 'is_active', 'date_created', 'date_update')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('place', 'serves_hot_dogs', 'serves_pizza', 'date_created', 'date_update')


class WaiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waiter
        fields = ('id', 'restaurant', 'name', 'date_created', 'date_update')                
