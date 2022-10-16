"""appmain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

router.register(r'task', views.TaskViewSet)

router.register(r'customers', views.CustomerViewSet)

router.register(r'products', views.ProductViewSet)

router.register(r'places', views.PlaceViewSet)
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'waiters', views.WaiterViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),             # LIST API
    # path('', views.index, name="index"),      # DEFAULT

    path('login', views.login, name="login"),
    path('sadmin/', admin.site.urls),        # DEFAULT

    path('api/tasks/', views.TaskList.as_view()),
    path('api/tasks/<int:pk>', views.TaskDetail.as_view()),

    path('api/customers/', views.CustomerList.as_view()),
    path('api/customers/<int:pk>', views.CustomerDetail.as_view()),

    path('api/products/', views.ProductList.as_view()),
    path('api/products/<int:pk>', views.ProductDetail.as_view()),

    path('api/places/', views.PlaceList.as_view()),
    path('api/places/<int:pk>', views.PlaceDetail.as_view()),

    path('api/restaurants/', views.RestaurantList.as_view()),
    path('api/restaurants/<int:pk>', views.RestaurantDetail.as_view()),

    path('api/waiters/', views.WaiterList.as_view()),
    path('api/waiters/<int:pk>', views.WaiterDetail.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


admin.site.site_header = "INNO Admin"
admin.site.site_title = "INNO Admin Portal"
admin.site.index_title = "Welcome to INNO Researcher Portal"
