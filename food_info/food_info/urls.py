"""
URL configuration for food_info project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
"""

from django.contrib import admin
from django.urls import path

from .views.food_item_list import food_item_list
from .views.views import new_food_item, food_item_from_image
from .views.api.food_item import ListFoodItems

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", food_item_list),
    path("new/", new_food_item),
    path("from-image/", food_item_from_image),
    path("api/items/", ListFoodItems.as_view()),
]
