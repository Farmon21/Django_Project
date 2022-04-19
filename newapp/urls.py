from django.urls import path
from .views import deleteTask, index, updateTask



urlpatterns = [
    path('', index, name='list'),
    path('update_task/<str:pk>/', updateTask, name='update_task'),
    path('detele/<str:pk>/', deleteTask, name='delete'),
]