from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('project/<str:slug>', views.project, name='project'),
    path('category/<str:category>', views.category, name='category'),
    path('categories/', views.categories, name='categories'),

]