from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('', views.projects),
    path('', views.tasks),
    path('about/', views.about),
    path('product/', views.product), 
    path('hello/<str:username>', views.hello),
    path('operacion/<int:numero>/', views.operacion),
    path('projects', views.projects),
    path('tasks/<int:id>', views.tasks),
]
