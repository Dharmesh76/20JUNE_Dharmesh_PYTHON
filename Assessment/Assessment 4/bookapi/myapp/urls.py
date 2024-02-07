from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('getall/',views.getall),
   path('get/<int:id>/',views.getId),
   path('delete/<int:id>/',views.delete_data),
   path('addbook',views.add_data),
   path('update/<int:id>/',views.update_data),
]